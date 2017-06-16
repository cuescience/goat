#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



requirements = [
    "behave",
]

test_requirements = [
    "behave",
]

setup(
    name='goat',
    version='0.3.2',
    description='Goat implements a behave matcher which uses python3 function annotations for step definitiions',
    author='Ilja Bauer',
    author_email='i.bauer@cuescience.de',
    url='https://github.com/cuescience/goat',
    packages=[
        'goat',
    ],
    package_dir={'goat':
                 'goat'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='goat',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='features',
    tests_require=test_requirements
)
