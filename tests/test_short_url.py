# -*- coding: utf-8 -*-

from random import randrange

from pytest import raises

import short_url





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
