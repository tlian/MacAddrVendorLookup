# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory
WORKDIR /mac-vendor-app

# Copy the current directory contents into the container at /mac-vendor-app
COPY . /mac-vendor-app

# Install the application
RUN pip install --trusted-host pypi.python.org .

# Get variables at build time
ARG MAL_APIKEY
ARG MAC_ADDRESS
ENV MAL_APIKEY=$MAL_APIKEY
ENV MAC_ADDRESS=$MAC_ADDRESS

# Run mac-vendor-lookup app when the container launches
CMD mac-vendor-lookup --macaddress ${MAC_ADDRESS} --api-key ${MAL_APIKEY}
