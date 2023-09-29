## Overview

Python-OC-Lettings-Fr is the application for Orange County Lettings.

This application has been modified to a modular structure. To allow access to the public, the application has a CircleCI pipeline (CI/CD) to containerize it and to deploy it on Heroku.

## Quick start

- Clone the repository
  - `cd /path/to/project`
  - `git clone https://github.com/TroadecJb/Python-OC-Lettings-FR.git`

- Create virtual environment with dependecies
  - `cd /path/to/project/Python-OC-Lettings-FR`
  - `python -m venv venv`
  - Activate the environment
    - on windows `venv\Scripts\activate`
    - on MacOS/Linux `source venv/bin/activate`
  - Install dependecies necessary to run the application
    - `pip install -r requirements.txt`
  - To deactivate the environment
    -`deactivate`

- Linting
  - `cd /path/to/Python-OC-Lettings-FR`
  - `source venv/bin/activate`
  - `flake8`

- Tests
  - `cd /path/to/Python-OC-Lettings-FR`
  - `source venv/bin/activate`
  - `pytest`

- Start the app
  - `cd /path/to/project/Python-OC-Lettings-FR`
  - Activate the environment
  - `python manage.py runserver`
  - From a web browser access the app with `http://localhost:8000`

- Access the admin panel
  - Go to `http://localhost:8000/admin`
  - Connect with user `admin` and password `Abc1234!`

## Requirements

Django==4.2.5  
coverage==7.3.1  
flake8==6.1.0  
gunicorn==21.2.0  
pytest-django==4.5.2  
sentry-sdk==1.31.0  
whitenoise==6.5.0  

Sentry needs [sqlalchemy extra](https://docs.sentry.io/platforms/python/configuration/integrations/sqlalchemy/)

See `requirements.txt` for more information

## CI/CD pipeline

The CI/CD pipeline is a series of steps to make the application available for the users.
In this case the CI/CD pipeline uses CircleCI.

The pipeline starts when a change is made on the Git repository.

The pipeline:

  - **Build** The application is compiled, using environment variables stored in CircleCI environment variables (SENTRY_DSN, SECRET_KEY, DOCKERHUB_API, DOCKERHUB_REPO, DOCKERHUB_USERNAME, HEROKU_TOKEN, HEROKU_APPNAME).

  - **Lint** The codebase is checked using flake8.

  - **Test** Using pytest, tests check functions results, behaviour and templates used.

  - **Coverage** The coverage stage checks for code coverage, aiming for at least 84% of the codebase tested.

  - **Push** This stage build the Docker image and pushes it to Dockerhub, only its master branch, if the previous stages (Build, Test, Coverage) went successfully.

  - **Deploy** The last stage, where the application is deployed to Heroku, only its master branch, if the previous stages (Build, Test, Coverage) went successfully.

The pipeline allows for a safer delivery of the application, using automated testing and deployment.

## Documentation

For more details about the codebase and procedures, see the documentation [here](https://oc-lettings-fr.readthedocs.io/en/latest/)