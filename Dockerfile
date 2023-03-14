# Set the base image
FROM python:3.9-alpine

# Install necessary libraries
RUN apk add --no-cache gcc musl-dev postgresql-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the app files to the working directory
# COPY . /app

# Set the environment variables for Flask and PostgreSQL

# Set the command to run the Flask app
# CMD ["flask", "run", "--host", "0.0.0.0"]
