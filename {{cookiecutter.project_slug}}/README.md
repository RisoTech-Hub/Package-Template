{{cookiecutter.project_name}}
=====

{{cookiecutter.description}}


Installation and usage
======================

Quick start
-----------

1. Add "{{cookiecutter.project_slug}}" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "{{cookiecutter.project_slug}}",
    ]


How to contribute
=================

Please make sure to update tests as appropriate.

Getting Started
---------------

1. Clone the repository

    - Run the following command in your terminal


    $ pre-commit install
    $ git update-index --assume-unchanged .idea/runConfigurations/* .idea/riso.iml


2. Prepare the environment

    - Create a virtual environment with Python 3.10 or higher and activate it

    $ cd riso
    $ pip install -r requirements.txt


3. Update following files

    - .envs/.local/.django
    - .envs/.local/.postgres

4. Then using pycharm runConfiguration to start coding


Useful commands
---------------

- Run test with coverage


    $ docker-compose -f riso/local.yml run --rm django pytest --cov --cov-report term-missing --cov-report html


Other information
=================

What's in this project?
-----------------------

This project is a Django project with a single app called "polls". The app
contains models for Questions and Choices, views to display Questions and
process votes, and tests to test the models and views.

The project also contains a single test to test the project's URLs.
