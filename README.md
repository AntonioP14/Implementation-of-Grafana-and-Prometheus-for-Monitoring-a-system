# Implementation-of-Grafana-and-Prometheus-for-Monitoring-a-system

# Monitoring Project

## Overview

This project implements a monitoring system using Docker, Prometheus, and Grafana. It monitors a sample Python application by collecting metrics through Prometheus and visualizing them with Grafana.

## Prerequisites

- **Docker**: Required to run containerized services. [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Manages multi-container Docker applications. [Install Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

- **`Dockerfile`**: Defines the Docker image for the Python application.
- **`docker-compose.yml`**: Configures and manages Prometheus, Grafana, and the Python application containers.
- **`prometheus.yaml`**: Prometheus configuration file.
- **`main.py`**: Python application exposing metrics.
- **`README.md`**: Project documentation.

## Setup Instructions

### Clone the Repository

## Steps to Deploy

### Build and Start Services

Navigate to the project directory and run:

    **docker-compose up --build**

This command will build the Docker images and start the Prometheus, Grafana, and Python application services.

### Access Services

- Prometheus: Access the web interface at http://localhost:9090.
- Grafana: Access the web interface at http://localhost:3000 using the default credentials:
    - Username: admin
    - Password: admin

### Configure Grafana

Add Prometheus Data Source

- Open Grafana in your browser.
- Navigate to Configuration (⚙️) -> Data Sources.
- Click "Add data source" and select "Prometheus".
- Set the URL to http://prometheus:9090.
- Click "Save & Test" to verify the connection.

Create a Dashboard

- Click the "+" icon on the sidebar and select "Dashboard".
- Click "Add new panel".
- Choose "Prometheus" as the data source.
- Enter your metric name (e.g., request_processing_seconds) in the query field.
- Customize the panel as desired and click "Apply".
- Save the dashboard with a descriptive name.

### Testing and Verification

- Prometheus: Verify metrics collection by querying http://localhost:9090 and checking if your metrics appear.
- Grafana: Ensure that the dashboards correctly visualize the metrics collected by Prometheus.




    
