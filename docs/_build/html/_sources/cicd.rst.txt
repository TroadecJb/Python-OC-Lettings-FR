CI/CD Pipeline
==============


| The CI/CD pipeline is a series of steps to make the application available for the users.
| In this case the CI/CD pipeline uses CircleCI.

The pipeline starts when a change is made on the Git repository.

The pipeline:

1. **Build** The application is compiled, using environment variables stored in CircleCI environment variables (SENTRY_DSN, SECRET_KEY, DOCKERHUB_API, DOCKERHUB_REPO, DOCKERHUB_USERNAME, HEROKU_TOKEN, HEROKU_APPNAME).
2. **Lint** The codebase is checked using flake8.
3. **Test** Using pytest, tests check functions results, behaviour and templates used.
4. **Coverage** The coverage stage checks for code coverage, aiming for at least 84% of the codebase tested.
5. **Push** This stage build the Docker image and pushes it to Dockerhub, only its master branch, if the previous stages (Build, Test, Coverage) went successfully.
6. **Deploy** The last stage, where the application is deployed to Heroku, only its master branch, if the previous stages (Build, Test, Coverage) went successfully.

The pipeline allows for a safer delivery of the application, using automated testing and deployment.


CircleCI
--------

    To use the pipeline, a CircleCI account is mendatory.
        #. Go to their official website https://circleci.com/
        #. CLick on ``Go to application``
        #. Create an account:
            | You can either choose to create an account with your email (you will have to connect to the github repository later to access it)
            | or use your github account to directly link the repository to CircleCI.
        
        If you created an account with your email:
            #. Create a new project and follow the instructions to connect to a Github repository

        If you created an account using your Github account:
            #. Create a project and select your Github repository to use

        #. Go to your project settings
        #. Select the menu Environment variables
        #. Add the following variables:
            - SECRET_KEY (same as the .env)
            - SENTRY_DSN (same as the .env)
            - DOCKERHUB_PASS (https://docs.docker.com/docker-hub/access-tokens/#create-an-access-token)
            - DOCKERHUB_REPO (the name of your image)
            - DOCKERHUB_USERNAME (your username's account)
            - HEROKU_API_KEY (under API Key in your account on heroku dashboard or from cli _here: https://help.heroku.com/PBGP6IDE/how-should-i-generate-an-api-key-that-allows-me-to-use-the-heroku-platform-api )
            - HEROKU_APP_NAME (name under which the app will be deployed on heroku)
        
        Now after each new commit on the main branch, the pipeline will start following each steps, deploying your new version of the application.

    To create an account on Heroku:
        #. Go to their official website https://www.heroku.com/
        #. Click on Sign up
        #. Fill the form
        #. Follow the instructions
