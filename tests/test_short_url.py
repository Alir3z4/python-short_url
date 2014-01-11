# -*- coding: utf-8 -*-
import unittest
from random import randrange

import short_url


class TestShortUrl(unittest.TestCase):

    def test_one(self):
        url = short_url.encode_url(12)
        self.assertEqual(url, 'jy7yj')
        key = short_url.decode_url(url)
        self.assertEqual(key, 12)

    def test_1000_random(self):
        for random_int in range(1000):
            random_int = randrange(100000000)
            url = short_url.encode_url(random_int)
            int_ = short_url.decode_url(url)
            self.assertEqual(random_int, int_)

    def test_custom_alphabet(self):
        encoder = short_url.UrlEncoder(alphabet='ab')
        url = encoder.encode_url(12)
        self.assertEqual(url, 'bbaaaaaaaaaaaaaaaaaaaa')
        key = encoder.decode_url('bbaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(key, 12)

    def test_short_alphabet(self):
        with self.assertRaises(AttributeError):
            short_url.UrlEncoder(alphabet='aa')
        with self.assertRaises(AttributeError):
            short_url.UrlEncoder(alphabet='a')
