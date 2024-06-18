FROM python:3.8-slim

# Install tzdata package
RUN apt-get update && apt-get install -y tzdata \
    # Clean up the apt cache to reduce image size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the timezone
ENV TZ=Asia/Seoul

# Install Python packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
