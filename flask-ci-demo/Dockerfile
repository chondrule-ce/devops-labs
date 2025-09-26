# Start from the lightweight Python image
FROM python:3.10-slim

# Create and set the working directory '/app' in the image
WORKDIR /app

# Copy to the current dir '/app', '.' means the current working dir
COPY requirements.txt .

# Install dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy to the current dir '/app'
COPY app.py .

# Inform Docker users that the containerized app uses port 5000
EXPOSE 5000

# Execute when the container starts
CMD ["python", "app.py"]