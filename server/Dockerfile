FROM python:3.11-slim

WORKDIR /app

# Install compiler for pandas/numpy if required
RUN apt-get update && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY code — uploads & output folders are excluded by .dockerignore
COPY . .

# Create empty folders for runtime
RUN mkdir -p uploads output

EXPOSE 5000

CMD ["python", "server.py"]
