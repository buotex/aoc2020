try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='aoc',
    packages=[
        'aoc',
    ],
)
