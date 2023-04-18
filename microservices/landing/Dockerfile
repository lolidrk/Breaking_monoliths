# Use the python:3.8-alpine base image
FROM python:3.8-alpine

RUN echo -e "http://nl.alpinelinux.org/alpine/v3.5/main\nhttp://nl.alpinelinux.org/alpine/v3.5/community" > /etc/apk/repositories

# Copy requirements.txt to /app/requirements.txt
COPY ./app/requirements.txt /app/requirements.txt

# Set working directory to /app
WORKDIR /app

# Run apk update and install necessary packages, upgrade pip, install requirements, and clean up cache
RUN apk update \
    && apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Copy contents of ./app to /app folder
COPY ./app /app

# Update Flask app code to use __name__ instead of _name_
RUN sed -i 's/_name__/__name__/g' /app/app.py

# Run the command python app.py
CMD ["python", "app.py"]

