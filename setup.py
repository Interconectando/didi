# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in didi/__init__.py
from didi import __version__ as version

setup(
	name='didi',
	version=version,
	description='App para gestión de flotillas de mobilidad DiDi.',
	author='Interconectando, Desarrollando y Automatizando, SAPI de CV',
	author_email='apps@interconectando.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
