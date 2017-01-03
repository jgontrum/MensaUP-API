# MensaUP API

API for the Uni Potsdam Mensa

The API can be reached under ```http://localhost:10010/api/```.

## Requirements

- Python 3.5: [Instructions](https://www.python.org/downloads/)

- virtualenv: [Instructions](https://virtualenv.pypa.io/en/stable/installation/)

## Installation

Run ```make``` for a local setup and then ```env/bin/start_debug``` to start the API in debug mode.

To start the uWSGI, run ```make start```

## Procedure

First, define your REST API in the configuration under ```/config/api.yml```, 
then add the Python logic for the *operationId* under /mensaup_api/api

## SwaggerUI

Go to [here](http://localhost:10010/api/ui) to view the brilliant SwaggerUI documentation of your API.

## Resources
### Connexion
[Documentation](https://connexion.readthedocs.io/en/latest/)
[Github](https://github.com/zalando/connexion)