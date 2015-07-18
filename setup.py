try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
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
