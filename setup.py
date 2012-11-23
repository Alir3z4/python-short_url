from distutils.core import setup

setup(
    name='short_url',
    version=".".join(map(str, __import__('short_url').__version__)),
    packages=['short_url',],
    url='https://github.com/Alir3z4/short_url',
    license='MIT',
    author='Michael Fogleman',
    author_email='michael.fogleman@gmail.com',
    description='Python implementation for generating Tiny URL- and bit.ly-like URLs.',
    long_description=open('README.rst').read(),
)
