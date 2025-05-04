# Use official Python 3 image
FROM python:3.11-slim

# Install C++ compiler and tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        g++ \
        cmake \
        && rm -rf /var/lib/apt/lists/*

# Set working directory inside the container to the project root
WORKDIR /python_for_dummies

# Copy all files into the container
COPY . /python_for_dummies

# Install Python packages if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Start bash by default
CMD ["bash"]
