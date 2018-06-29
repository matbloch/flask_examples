FROM python:3

# File Author / Maintainer
MAINTAINER Matthias Bloch

# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && pip3 install -r /tmp/requirements.txt

# inform about port listening (use -p when you start the container)
EXPOSE 8080

# Add demo app
COPY ./web /web
WORKDIR /web

CMD ["python", "run.py", "-p 8080"]