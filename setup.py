#!/usr/bin/env python3

from setuptools import setup
from hello import __version__

with open('README.rst') as f:
    readme = f.read()
with open('CHANGES.rst') as f:
    changes = f.read()


setup(
    name='hello_world_1989',  # The name of the package
    version=__version__,  # the version number of the package
    description='A module to reply hello to a user',
    # A short description of package
    long_description=readme + '\n\n' + changes,
    # A long description of package
    author='Olly Middleton',  # The maintainer
    author_email='ollymiddleton2@gmail.com',  # The maintainer's email address
    url='https://github.com/Ollymid/hello_world_1989',  # The package's website
    py_modules=['hello', ],  # The python modules to include
    license='MIT',  # The license type
    entry_points={  # links to "hello" command with a function to call
        'console_scripts': ['hello=hello:main'],
    }
)
