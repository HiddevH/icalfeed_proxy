# iCal feed proxy
This repository contains a 'proxy' to retrieve an iCal feed from external location and forward it to the requester.

Why? Because some booking websites block the opening of their iCal feed by certain tools, so this is a workaround for that.

In the folder `app` you will find:
- The python script `api.py` which handles the actual API requests
- requirements.txt which contains the Python packages used
- Dockerfile with the instructions to build the container

## Application
Within the folder `app` there is a script called `api.py`. This script is basically a Flask application which listens on port `5002` for API requests.
The API requests possible are:
- `/icalfeed` which returns an iCal feed which is passed from ENV `ICAL_FEED`

## Dockerfile
The API is supposed to live in a Docker container. A brief overview of its contents:
- Use the lightweight `python:3.7-slim-buster` distribution
- Copy requirements.txt and pip install on it
- Create a non-root User to run the scripts (according to some best practices found at https://pythonspeed.com/docker/)
- Set environment variables
- Expose port 5002
- Run Flask

## Docker Compose
I use this flask app with Docker Compose, an example docker-compose is:
```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5002:5002"
    volumes:
      - .:/src
    environment:
      FLASK_ENV: production
      ICAL_FEED: icalfeedhere
```

## Usage

```webhook
<ip>:5002/icalfeed
```
Should return an ical feed