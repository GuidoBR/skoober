# -*- coding: utf-8 -*-
from os.path import dirname, join
from setuptools import setup

with open(join(dirname(__file__), 'requirements.txt'), 'rb') as f:
    requirements = f.read().splitlines()

setup(name='skoober',
      version='0.1',
      license='MIT',
      description='Extract user\'s data from Skoob.com.br',
      author='Guido Luz Percú',
      author_email='guidopercu@gmail.com',
      url='http://github.com/GuidoBR/skoober',
      platforms=['Any'],
      py_modules=['skoober'],
      install_requires=requirements,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          ],
      )
