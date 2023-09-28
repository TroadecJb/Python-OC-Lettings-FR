Installing the app
==================

Local use in development
------------------------

* Requirements
    - `Link Python <https://www.python.org/>`_ 3.11 or superior
    - `Link Github <https://github.com/>`_ account
    - `Link Git CLI <https://git-scm.com/downloads>`_

* Python installation :
    
    - For Windows and MacOS:

        | Visit the official Python website at https://www.python.org/.
        | Click on the "Downloads" button and download the latest version of Python.

        | After the installer is downloaded, run it.
        | On the first installer page, make sure you check the box "Add Python to PATH".
        | This will allow you to run Python from the command line.

    - For Linux:

        | Most Linux distributions come with Python pre-installed.
        | You can check if Python is installed by opening a terminal and typing
        | ``python --version`` or ``python3 --version``.

        | If Python isn't installed, you can install it using your distribution's package manager.
        | For example, on Ubuntu, you can run ``sudo apt-get update`` followed by ``sudo apt-get install python3``.

* Github account :

    #. Got to Github website at https://github.com/
    #. Sign up
    #. Follow the instructions

* Git installation :

    - For Windows:
        #. Go to the official git website https://git-scm.com/downloads and download the installer for Windows.
        #. During the installation, you can leave all the default options,
            unless you have specific preferences.
        #. Check if Git was installed correctly:
            Open a terminal and run ``git --version``.
            This should show the version of Git that has been installed.

    - For MacOS:
        #. You can install git on macOS using Homebrew, a package manager for macOS.
            If you haven't installed it yet, you can get it at https://brew.sh/ .
        #. Once you've installed Homebrew, open a terminal and run the following command:
            ``brew install git``.
        #. Check if Git was installed correctly by running ``git --version`` in the terminal.

    for Linux:
        #. On most Linux distributions, Git is available in the system's package manager.
            For example, on Debian or Ubuntu, you can install
            git by running ``sudo apt-get install git`` in a terminal.
        #. Check if Git was installed correctly by running ``git --version`` in the terminal.

* Environment variables

    Create a ``.env`` file in the root folder of the project.
    Add two variables:
    - SECRET_KEY='your_secret_key_here'
    - SENTRY_DSN='your_sentry_dsn_here'

    - Sentry account:
        #. If you do not have a Sentry account go to their official website https://sentry.io/welcome/
        #. Click on ``GET STARTED``
        #. Fill the form
        #. Create a new project
        #. Select DJANGO in the platform selection
        #. Set the alert frequency
        #. Name the project and the terminal
        #. After clicking ``Create Project`` in the Configure SDK section copy the value of the variable ``dsn``.



Local use in production
-----------------------
* Requirements
    - `Link Python <https://www.python.org/>`_ 3.11 or superior
    - `Link Github <https://github.com/>`_ account
    - `Link Git CLI <https://git-scm.com/downloads>`_
    - `Link Docker <https://www.docker.com/>`_

* Docker installation :

    #. Go to the official Docker website https://www.docker.com/
    #. Click the download button, the website will automatically recommend the version for your operating system.
    #. Install it by following the instructions provided.

* Docker account :

    #. Go to Dockerhub website https://hub.docker.com/
    #. Fill the form ``Create your account``
    #. Follow the instructions

* Usage :

    Start Docker on your machine.
    You can know build an image of the app from the terminal and running locally.
    The image specifications are set with the Dockerfile at the root of the project.
    For how to build an image follow this link https://docs.docker.com/build/building/packaging/#building
    