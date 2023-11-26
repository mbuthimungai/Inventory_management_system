# Inventory Management System API

## Overview
This project is an inventory management system API developed using Django Rest Framework (DRF). It's designed to handle various aspects of inventory management, including items, stock, transactions, categories, and suppliers.

## Features
- **Items Management**: Add, retrieve, update, and delete inventory items.
- **Stock Management**: Manage stock levels for each item.
- **Transaction Recording**: Record and retrieve purchase/sale transactions.
- **Category and Supplier Management**: Organize items into categories and manage supplier details.

## To-Do and Contributions

- **Authentication and Authorization**: This feature is critical for securing the API. We plan to implement robust authentication and authorization mechanisms.

- **Payment Gateway Integration (M-PESA)**: We aim to integrate M-PESA as a payment gateway. This will facilitate seamless sales transactions within the system, making it more efficient for users in regions where M-PESA is a popular payment method.

- **Contributing**: Contributions are welcome, especially from individuals with experience in Django Rest Framework, authentication, authorization, and payment systems like M-PESA. If you're interested in contributing to these areas, please reach out to me via Twitter([https://twitter.com/MungaiMbuthi]) for collaboration.

## Installation

This project is containerized using Docker, ensuring a consistent and isolated environment for development and deployment.

### Prerequisites

- **Docker**: You need to have Docker installed on your local machine. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

### Getting Started with Docker
If you're new to Docker, I recommend reading these articles for a solid introduction:
- [Getting started with Docker](https://dev.to/mbuthi/docker-2oge)
- [DevOps with Fast API & PostgreSQL: How to containerize Fast API Application with Docker](https://dev.to/mbuthi/devops-with-fast-api-postgresql-how-to-containerize-fast-api-application-with-docker-1jdb)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mbuthi/Inventory_management_system.git
   ```

2. **Build the Docker Containers**:
   Navigate to the root directory of the project and run:
   ```bash
   docker-compose -f docker-compose.yml build --no-cache
   ```

3. **Start the Containers**:
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```

### Database

- The project uses **PostgreSQL** as its database. The Docker setup includes the PostgreSQL container, so you do not need to install it separately.

### Running the Application

Once the Docker containers are up and running, the Inventory Management System API will be accessible at the designated port.

In your browser, you can access the API through HTTP://localhost:8000/api/v1

## API Endpoints

### Items
- `POST /items`: Add a new inventory item.
- `GET /items`: Retrieve a list of all inventory items.

### Stock
- `POST /stock`: Add stock for an item.
- `GET /stock/{itemId}`: Retrieve current stock for an item.

### Transactions
- `POST /transactions`: Record a new transaction.
- `GET /transactions`: Retrieve all transactions.

_More endpoints are detailed in the documentation._

## Project Structure

- `models/`: Contains the models for the API.
- `serializers/`: Contains serializers for model instances.
- `views/`: Contains views for handling requests.
- `urls.py`: URL declarations for the API endpoints.
