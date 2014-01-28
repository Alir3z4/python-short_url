# -*- coding: utf-8 -*-

import os
from random import randrange

from pytest import raises

import short_url


TEST_DATA = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEST_DATA = os.path.join(TEST_DATA, 'tests/data')


def generate_test_data(count=10000):
    result = {}

    for i in range(1000):
        value = short_url.encode_url(i)
        result[i] = value

    while len(result) < count:
        random_int = randrange(1000000)
        value = short_url.encode_url(random_int)
        result[random_int] = value

    with open(os.path.join(TEST_DATA, 'key_values.txt'), 'w') as f:
        for k, v in result.items():
            f.write('%s:%s\n' % (k, v))

# generate_test_data()


def load_data(filename):
    filename = os.path.join(TEST_DATA, filename)
    with open(filename, 'r') as f:
        return f.read().splitlines()


def test_custom_alphabet():
    encoder = short_url.UrlEncoder(alphabet='ab')
    url = encoder.encode_url(12)
    assert url == 'bbaaaaaaaaaaaaaaaaaaaa'
    key = encoder.decode_url('bbaaaaaaaaaaaaaaaaaaaa')
    assert key == 12


def test_too_short_alphabet():
    with raises(AttributeError):
        short_url.UrlEncoder(alphabet='aa')
    with raises(AttributeError):
        short_url.UrlEncoder(alphabet='a')


def test_calculated_values():
    lines = load_data('key_values.txt')
    for line in lines:
        key, value = line.split(':')
        key = int(key)
        encoded_value = short_url.encode_url(key)
        assert encoded_value == value
        decoded_key = short_url.decode_url(encoded_value)
        assert decoded_key == key
