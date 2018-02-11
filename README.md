# latrine
Web app for finding hygiene resources in Portland, OR

# Setup

## Instructions for the Team
1. Fork and clone this project.
### For Django:
2. Django requires Python to run. Download Python3 at https://www.python.org/downloads/ or with your operating system's package manager.
3. You may need to install ```pip``` (Python package manager) if you don't have it already. Follow [pip installation](http://pip.readthedocs.io/en/stable/installing/#install-pip).
4. Install ```virtualenv``` with ```pip``` (pip is already installed if you're using the latest version of Python). ```virtualenv``` is a tool to create isolated Python environments.
    ```sh
    $ [sudo] pip install virtualenv
    ```
5. Create and activate your virtual environment.
    ```sh
    $ virtualenv env --no-site-packages
    $ source env/bin/activate
    ```
6. After you’ve created and activated a virtual environment, install Django. The recommended way to install Django is with ```pip```:
    ```sh
    $ [sudo] pip install Django
    ```
7. Navigate to the Django project directory ```latrine_django``` and apply migrations:
    ```sh
    $ python manage.py migrate
    ```
8. To start the development server, run:
    ```sh
    $ python manage.py runserver
    ```
9. Open http://localhost:8000 in your browser to view the app.
### For React:
The React app will live in the ```/frontend``` folder and talk to Django over an API.
1. You’ll need to have [Node.js](http://nodejs.org/en/) on your local development machine. The Node.js package comes with ```npm```, the package manager for JavaScript.
1. ```cd``` into the ```/frontend``` directory and install the existing setup:
    ```sh
    $ cd ./frontend
    $ npm install
    ```
2. Install ```axios```. It's a library for sending http requests (similar to ajax), which will be used for handling API calls.
    ```sh
    $ npm install axios --save
    ```
3. To start the development server, run:
    ```sh
    $ npm start
    ```
4. Open http://localhost:3000 in your browser to view the app.

# Deploy

# Run Tests

# Contribute!
