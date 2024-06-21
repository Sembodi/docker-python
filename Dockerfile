# Dockerfile
FROM python:3.9

# Set working directory
WORKDIR ./src

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /src

# Command to run the application
# CMD ["python", "-u", "./src/main.py"]
CMD ["sh", "-c", "python -u ./src/main.py && python -u ./src/dataProcessing.py"]
