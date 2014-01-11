# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='short_url',
    py_modules=['short_url'],
    version=".".join(map(str, __import__('short_url').__version__)),
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/Alir3z4/short_url',
    license='MIT',
    author='Michael Fogleman',
    author_email='michael.fogleman@gmail.com',
    maintainer='Alireza Savand',
    maintainer_email='alireza.savand@gmail.com',
    description='Python implementation for generating Tiny URL- and bit.ly-like URLs.',
    long_description=open('README.rst').read(),
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development'
    ],
)
