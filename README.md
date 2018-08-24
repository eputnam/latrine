# latrine
Web app for finding hygiene resources in Portland, OR

# Setup

## Instructions for the Team
1. Fork and clone this project.
### For Django:
## Run with Docker and Docker Compose:
Uncomment PostgreSQL database settings in ```settings.py``` and comment out sqlite3 settings above.
In the root folder run:
```sh
$ [sudo] docker compose up --build -d
```
Open http://localhost:8000 in your browser to view the list of available endpoints (you might need to wait around 30 seconds until all management commands inside the Django container are complete).
To stop and remove the containers, use:
```sh
$ [sudo] docker compose down
```
## Run Django without Docker:
1. Django requires Python to run. Download Python3 at https://www.python.org/downloads/ or with your operating system's package manager.
2. You may need to install ```pip``` (Python package manager) if you don't have it already. Follow [pip installation](http://pip.readthedocs.io/en/stable/installing/#install-pip).
3. Install ```virtualenv``` with ```pip``` (pip is already installed if you're using the latest version of Python). ```virtualenv``` is a tool to create isolated Python environments.
    ```sh
    $ [sudo] pip install virtualenv
    ```
4. Create and activate your virtual environment.
    ```sh
    $ virtualenv env --no-site-packages
    $ source env/bin/activate
    ```
5. After you’ve created and activated a virtual environment, Navigate to the Django project directory ```latrine_django```. Install Django and other dependences:
    ```sh
    $ [sudo] pip install -r requirements.txt
    ```
6. Apply migrations:
    ```sh
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```
7. Apply fixtures to populate the database with sample data:
    ```sh
    $ python manage.py loaddata fixturefile.json
    ```
8. Populate the database with the RefugeRestrooms public data:
    ```sh
    $ python manage.py get_restrooms
    ```
9. To have access to the Django admin site, run:
    ```sh
    $ python manage.py createsuperuser
    ```
Follow the prompts to set up your login and password.
10. To start the development server, run:
    ```sh
    $ python manage.py runserver
    ```
11. Open http://localhost:8000 in your browser to view the list of available endpoints.
### For React:
The React app will live in the ```/frontend``` folder and talk to Django over an API.
1. You’ll need to have [Node.js](http://nodejs.org/en/) on your local development machine. The Node.js package comes with ```npm```, the package manager for JavaScript.
2. ```cd``` into the ```/frontend``` directory and install the existing setup:
    ```sh
    $ cd ./frontend
    $ npm install
    ```
3. To start the development server, run:
    ```sh
    $ npm start
    ```
4. Open http://localhost:3000 in your browser to view the app.

# Deploy

# Run Tests

## For Django

Cd into ```/latrine_django``` and run:
```sh
$ python manage.py test
```
If you use Docker and Docker Compose, spin up containers and run:
```sh
[sudo] docker-compose run latrine-django python manage.py test
```
# Contribute!

Check out [CONTRIBUTING.md](CONTRIBUTING.md) for details.
