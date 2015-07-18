# -*- coding: utf-8 -*-
from setuptools import setup

requirements = [
    'cffi==1.1.2',
    'cryptography==0.9.3',
    'cssselect==0.9.1',
    'enum34==1.0.4',
    'idna==2.0',
    'ipaddress==1.0.14',
    'loginform==1.0',
    'lxml==3.4.4',
    'pyasn1==0.1.8',
    'pycparser==2.14',
    'pyOpenSSL==0.15.1',
    'queuelib==1.2.2',
    'Scrapy==1.0.1',
    'six==1.9.0',
    'Twisted==15.2.1',
    'w3lib==1.11.0',
    'zope.interface==4.1.2',
]

setup(name='skoober',
      version='0.2',
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
