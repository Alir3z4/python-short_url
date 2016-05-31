Short URL Generator
===================

.. image:: https://travis-ci.org/Alir3z4/python-short_url.png
   :alt: travis-cli tests status for short_url
   :target: https://travis-ci.org/Alir3z4/python-short_url
   
.. image:: http://badge.kloud51.com/pypi/v/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Version

.. image:: http://badge.kloud51.com/pypi/s/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Status

.. image:: http://badge.kloud51.com/pypi/l/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI License

.. image:: http://badge.kloud51.com/pypi/f/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Format

.. image:: http://badge.kloud51.com/pypi/p/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Py_versions

.. image:: http://badge.kloud51.com/pypi/i/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Implementation

.. image:: http://badge.kloud51.com/pypi/e/short_url.svg
    :target: https://pypi.python.org/pypi/short_url
    :alt: PyPI Egg

Python implementation for generating Tiny URL- and bit.ly-like URLs.

A bit-shuffling approach is used to avoid generating consecutive, predictable
URLs.  However, the algorithm is deterministic and will guarantee that no
collisions will occur.

The URL alphabet is fully customizable and may contain any number of
characters.  By default, digits and lower-case letters are used, with
some removed to avoid confusion between characters like o, O and 0.  The
default alphabet is shuffled and has a prime number of characters to further
improve the results of the algorithm.

The block size specifies how many bits will be shuffled.  The lower BLOCK_SIZE
bits are reversed.  Any bits higher than BLOCK_SIZE will remain as is.
BLOCK_SIZE of 0 will leave all bits unaffected and the algorithm will simply
be converting your integer to a different base.

The intended use is that incrementing, consecutive integers will be used as
keys to generate the short URLs.  For example, when creating a new URL, the
unique integer ID assigned by a database could be used to generate the URL
by using this module.  Or a simple counter may be used.  As long as the same
integer is not used twice, the same short URL will not be generated twice.

The module supports both encoding and decoding of URLs. The min_length
parameter allows you to pad the URL if you want it to be a specific length.

Sample Usage:

>>> import short_url
>>> url = short_url.encode_url(12)
>>> print url
LhKA
>>> key = short_url.decode_url(url)
>>> print key
12

Use the functions in the top-level of the module to use the default encoder.
Otherwise, you may create your own UrlEncoder object and use its encode_url
and decode_url methods.


Install
-------

**short_url** is also available at pypi:

http://pypi.python.org/pypi/short_url

Give a try to your finger:

::

    $ pip install short_url

And done ;)


Tests
-----

``short_url`` is tested on both `python2` and `python3`, to run the tests:

::

    $ tox


----

========== ======
Source      https://github.com/Alir3z4/short_url
Website     http://alir3z4.github.com/short_url
Issues      https://github.com/Alir3z4/short_url/issues
PyPi        http://pypi.python.org/pypi/short_url
Author      Michael Fogleman
Maintainer  Alireza Savand
License     MIT
Link        http://code.activestate.com/recipes/576918/
========== ======

