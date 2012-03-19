#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-template-bootstrap",
    version = "0.1",
    license = 'BSD',
    description = "A django template based on twitter's bootstrap project.",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
