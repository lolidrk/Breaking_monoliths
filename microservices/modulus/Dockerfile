# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the port for the app
EXPOSE 5055

# Define environment variable
ENV NAME Modulus

# Run the command to start the app
CMD ["python", "app.py"]
