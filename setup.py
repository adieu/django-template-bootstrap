#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="django-template-bootstrap",
    version="0.2.8",
    license='BSD',
    description="A django template based on twitter's bootstrap project.",
    author='Ivan Diao',
    author_email='adieu@adieu.me',
    url='http://github.com/adieu/django-template-bootstrap',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
