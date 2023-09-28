Quick start
===========


* Clone the repository
    - ``cd /path/to/project``
    - ``git clone https://github.com/TroadecJb/Python-OC-Lettings-FR.git``

* Create virtual environment with dependecies
    - ``cd /path/to/project/Python-OC-Lettings-FR``
    - ``python -m venv venv``
    - Activate the environment
        - on windows ``venv\Scripts\activate``
        - on MacOS/Linux ``source venv/bin/activate``
    - Install dependecies necessary to run the application
        ``pip install -r requirements.txt```
    - To deactivate the environment
        - ``deactivate``

* Linting
    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``source venv/bin/activate``
    - ``flake8``

* Tests
    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``source venv/bin/activate``
    - ``pytest``

* Start the app
    - ``cd /path/to/project/Python-OC-Lettings-FR``
    - Activate the environment
    - ``python manage.py runserver``
    - From a web browser access the app with ``http://localhost:8000``



