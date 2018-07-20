FROM python:3

# File Author / Maintainer
MAINTAINER Matthias Bloch

# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && pip3 install -r /tmp/requirements.txt

# inform about port listening (use -p when you start the container)
EXPOSE 80

# Add demo app
COPY ./server /src
WORKDIR /src

CMD ["python", "run.py", "-p 80"]