# Dockerfile
FROM python:3.9

# Set working directory
WORKDIR /src

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Command to run the application
CMD ["python", "./src/main.py"]
