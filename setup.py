#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup function for the package."""

from setuptools import setup, find_namespace_packages

setup(
    name='gbj_hw',
    version='1.4.1',
    description='Python libraries for hardware support.',
    long_description=(
        'Modules suitable for utilizing Pi microcomputers,'
        'system buses, and sensors in python console applications.'
        'The package includes simulators for them for development of Windows.'
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Hardware',
    ],
    keywords='pi, orangepi, raspberrypi, nanopi',
    url='http://github.com/mrkalePythonLib/gbj_hw',
    author='Libor Gabaj',
    author_email='libor.gabaj@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
