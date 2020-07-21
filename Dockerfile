FROM python:3.7-slim-buster

COPY requirements.txt /tmp/

# Install app dependencies
RUN pip install -r /tmp/requirements.txt

# Create non-root User to run scripts
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Bundle app source
COPY api.py /src/

# Set environment variables
ENV FLASK_APP /src/api.py
ENV FLASK_RUN_HOST 0.0.0.0

# Expose port
EXPOSE  5002

# Run flask
CMD ["flask", "run"]
