FROM python:3.8-alpine

# Change the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app

# Install the dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the remaining files
COPY . /app
