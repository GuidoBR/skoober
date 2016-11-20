# -*- coding: utf-8 -*-
from setuptools import setup

requirements = [
]

setup(name='skoober',
      version='0.4',
      license='MIT',
      description='Extract user\'s books from Skoob.com.br',
      author='Guido Luz Percú',
      author_email='guidopercu@gmail.com',
      url='http://github.com/GuidoBR/skoober',
      platforms=['Any'],
      py_modules=['skoober'],
      install_requires=requirements,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      )
