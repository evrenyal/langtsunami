# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download the SpaCy Chinese model
RUN python -m spacy download zh_core_web_sm

# Copy the rest of the application code into the container at /app
COPY . /app

# Set the entry point to your main Python script
CMD ["python", "langtsunami.py"]
