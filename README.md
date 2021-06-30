# Software development proficiency test - Authorization Problem

This repository contains some templates for the authorization problem. The purpose of these files is to provide you with
some fundamentals for running the client and application.

The problem description can be found [in this attached PDF](TTE-Softwaredevelopmentproficiencytest-240621-0830.pdf).

The application is a flask based shell running on port 5001.

The client is just a python script that uses the `requests` python library to make a call to application's api endpoint.

You are free to add, remove, modify or do whatever you want to all files.

## Setup

It's assumed that the python environment will be `python3.9`, otherwise please specify which python version.

The easiest way to create a virtual environment (on linux) would be to use `virtualenv`

To create a virtual environment called `venv` using `python3.9` run

```bash
virtualenv -p python3.9 venv
```

To activate the virtual enviroment run

```bash
# Assuming you're using bash shell
source venv/bin/activate
```

Then to install the template dependencies you can use

```bash
# Using requirements.txt
pip install -r requirements.txt
```

## How to run the code

To start the application server first activate the virtual environment and run

```bash
python mocked_application.py
```

This will start the application template on port 5001 in debug mode.

After this, using a different terminal, run the client script with the command

```bash
python mocked_client.py
```

Which will simulate the client trying to make a request. If everything goes to plan, this will output

```bash
# Expected output from running `python mocked_client.py`
Request successful. Response was: '{'secret-data': 'very very secret'}'
```


## Endpoints
To call an endpoint of an application, user needs to set source as service name and api-token in the header.
Based on the permission, user can read data if the service has `can-access-data` permissions.

User with `can-create-service` can also add services, using `/add_service` endpoint.

## How to run tests

A sample (dummy) test file has been included under `tests` using the `unittest` framework, feel free to add more tests
or change testing framework.

To run all test files under `tests` using `unittest`, run:

```bash
python -m unittest discovery -s tests
```
