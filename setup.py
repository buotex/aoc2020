try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='aoc2020',
    packages=[
        'aoc2020',
    ],
)