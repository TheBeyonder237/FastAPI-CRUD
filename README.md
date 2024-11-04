# FastAPI CRUD Project

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

## Introduction
Follow these steps to set up and run your FastAPI project.

## Prerequisites
Ensure you have the following installed:
- **Python** >= 3.10
- **PostgreSQL**
- **Redis**

## Project Setup
1. Clone the project repository:
   ```bash
   git clone https://github.com/TheBeyonder237/FastAPI-CRUD.git
   ```

2. Navigate to the project directory:
   ```bash
   cd fastapi-beyond-CRUD/
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables by copying the example configuration:
   ```bash
   cp .env.example .env
   ```

6. Run database migrations to initialize the database schema:
   ```bash
   alembic upgrade head
   ```

7. Open a new terminal, activate your virtual environment, and start the Celery worker (Linux/Unix shell):
   ```bash
   sh runworker.sh
   ```

## Running the Application
To start the application:
```bash
fastapi dev src/
```

### Alternatively, Run the Application with Docker
```bash
docker compose up -d
```

## Running Tests
Run the tests using the following command:
```bash
pytest
```

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.
