# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at /app
COPY . .

# Install Flask
RUN pip install Flask


# Run the Flask application
# CMD ["flask", "--app", "app", "run","--host=0.0.0.0"]
