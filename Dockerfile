# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install required dependencies
RUN pip install fastapi pillow numpy tensorflow uvicorn python-multipart

# Copy the letter_images folder into the container at /app/letter_images
COPY letter_images /app/letter_images

# Expose port 80
EXPOSE 80

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
