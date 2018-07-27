FROM python:3.6
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /var/lib/latrine_django/
EXPOSE 8000
CMD . /usr/src/app/startserver.sh
