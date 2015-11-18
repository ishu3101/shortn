#!/usr/bin/env python

from setuptools import setup

setup(name='shortn',
      version='0.0.1',
      description='Shorten url using bit.ly, j.mp, t.cn, is.gd, v.gd, tiny.cc.',
      author='ishu3101',
      author_email='ishu3101@hotmail.com',
      license='MIT',
      long_description=open("README.md").read(),
      keywords = "shorten url_shortener shortener short",
      url='http://github.com/ishu3101/shortn',
      py_modules=['shortn'],
      entry_points = {
        'console_scripts': [
            'shortn = shortn:main'
        ],
      }
)