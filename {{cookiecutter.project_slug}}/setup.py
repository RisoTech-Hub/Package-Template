#!/usr/bin/env python
from distutils.util import convert_path

from setuptools import find_packages, setup


main_ns = {}
ver_path = convert_path("{{cookiecutter.project_slug}}/__init__.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="riso-{{cookiecutter.project_slug}}",
    version=main_ns["__version__"],
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.email}}",
    url="{{cookiecutter.repo_url}}",
    packages=find_packages(exclude=["*tests*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment ::  Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    include_package_data=True,
    python_requires=">=3.11",
    install_requires=[
        "Django==4.2",
    ]
)
