# Install This Plugin

To install the LuQY Pro NOMAD Plugin, follow these steps:

## Prerequisites

Ensure you have Docker installed on your machine. You will also need access to a NOMAD Oasis instance or a local NOMAD installation.

## Step 1: Create the `plugins.txt` File

In the `docker` directory, create a file named `plugins.txt` with the following content:

```
git+https://github.com/QYBBelonovskii/nomad-luqy-plugin.git@main
```

This file specifies the source from which the plugin will be installed.

## Step 2: Create the `Dockerfile.plugins`

In the `docker` directory, create a file named `Dockerfile.plugins` with the following content:

```
FROM ghcr.io/fairmat-nfdi/nomad-distro-template:main

USER root

RUN (command -v apk >/dev/null 2>&1 && apk add --no-cache git) || \
    (apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*)

COPY plugins.txt /tmp/plugins.txt

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1
RUN /opt/venv/bin/python3 -m ensurepip --upgrade || true && \
    /opt/venv/bin/python3 -m pip install --upgrade pip setuptools wheel && \
    /opt/venv/bin/python3 -m pip install -r /tmp/plugins.txt

USER 1000:1000
```

This file defines the Docker image for the plugin, installs Git, and sets up the required Python packages.

## Step 3: Build the Docker Image

Navigate to the `docker` directory in your terminal and run the following command to build the Docker image:

```
docker build -t my-nomad-oasis:with-luqy -f Dockerfile.plugins .
```

This command builds the Docker image using the `Dockerfile.plugins` you created.

## Step 4: Update the `docker-compose.yaml` File

In the `deployment` directory, open the `docker-compose.yaml` file and ensure it includes the following services configuration:

```yaml
version: '3.8'

services:
  app:
    image: my-nomad-oasis:with-luqy
    # Additional configuration for the app service

  worker:
    image: my-nomad-oasis:with-luqy
    # Additional configuration for the worker service

  north:
    image: my-nomad-oasis:with-luqy
    # Additional configuration for the north service
```

This configuration specifies that the app, worker, and north services will use the custom image you built.

## Step 5: Start the Services

Finally, navigate to the `deployment` directory and run the following command to start the services:

```
docker-compose up
```

This command will start the NOMAD services with the LuQY Pro plugin installed.

You are now ready to use the LuQY Pro NOMAD Plugin!
