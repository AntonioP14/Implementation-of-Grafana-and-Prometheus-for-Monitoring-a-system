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

### 1. Clone the Repository

2. Docker Configuration
Dockerfile

The Dockerfile sets up the environment for the Python application:
