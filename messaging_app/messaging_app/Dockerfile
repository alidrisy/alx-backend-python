# Use official Python image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside container
WORKDIR /app

# Copy requirements file
COPY Requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r Requirements.txt

# Copy the project code
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run migrations and start the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
