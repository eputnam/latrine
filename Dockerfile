# base image
FROM python:latest

# move project files from localhost
COPY . latrine/

# expose port 8000 for django interface
EXPOSE 8000

# change working directory
WORKDIR latrine/latrine_django/

# install packages from requirements file
RUN pip install -r requirements.txt

# start the django server
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

