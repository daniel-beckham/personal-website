FROM python:3.8-alpine

# Set the build-time variables
ARG DJANGO_SECRET_KEY
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_USERNAME

# Set the environment variables
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DJANGO_SUPERUSER_EMAIL $DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD $DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_USERNAME $DJANGO_SUPERUSER_USERNAME

# Change the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app

# Install the dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the remaining files
COPY . /app

# Collect the static files
RUN python manage.py collectstatic

# Apply the migrations
RUN python manage.py migrate

# Populate the database
RUN python manage.py loaddata projects.json

# Create the superuser
RUN python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
