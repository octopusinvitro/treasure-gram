[![Build Status](https://travis-ci.org/octopusinvitro/treasure-gram.svg?branch=master)](https://travis-ci.org/octopusinvitro/treasure-gram)
[![build status](https://gitlab.com/octopusinvitro/treasure-gram/badges/master/build.svg)](https://gitlab.com/octopusinvitro/treasure-gram/commits/master)


# Treasure Gram

![Screenshot](screenshot.png)

A project to play with Django.

This project was created with Python 3.4 and Django 1.10.0.


## Install

Clone the repo and install all dependencies:

```bash
cd treasure-gram/Treasuregram
pip install -r requirements.txt
```

## Run the migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Run the tests

```
python3 manage.py test
```

## Start the server:

```bash
python3 manage.py runserver
```

And go to <http://localhost:8000/>


## Concepts covered

* Database migrations
* Static files
* Routes and settings
* Passing contexts
* Templating language
* Template inheritance
* Form-Model mapping and sending data to the server
* Image uploading
* Registering admin with models
* One to many relationship User-Treasures
* User pages
* User authentication
* AJAX communicating with views
* Tests with unittest
* Continuous Integration for Travis and gitlab-ci
