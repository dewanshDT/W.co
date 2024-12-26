# Use Python 3.8 slim image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create output directory with proper permissions
RUN mkdir -p /app/output && chmod 777 /app/output

# Copy the rest of the application
COPY src/ ./src/
COPY data/ ./data/

# Expose port
EXPOSE 8501

# Run the Flask app
CMD ["python", "src/app.py"] 