#!/bin/bash

apt update

# Install JDK 17
sudo apt install openjdk-17-jdk

# Setup JAVA_HOME path for Spark
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# Or for OpenJDK 11

# export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
PATH=$JAVA_HOME/bin:$PATH

