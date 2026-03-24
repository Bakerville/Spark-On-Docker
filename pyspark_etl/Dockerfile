FROM ubuntu:latest

# Install OpenJDK 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-pip python3.12-venv&& \
    rm -rf /var/lib/apt/lists/*

# Create Working Directory
WORKDIR /code
COPY requirements.txt ./
    
# Create my-env virtual enviroment
RUN python3 -m venv my-env

# Install essential package
RUN ./my-env/bin/pip install -r requirements.txt

# Copy all files in current workdir to docker 
COPY ./ ./

CMD ["./my-env/bin/python3", "main.py"]


