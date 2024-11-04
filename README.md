
# Books API

## Description
This is a REST API for a book review web service that enables users to create, manage, and review books. The API includes authentication features for user management and token-based access, allowing for secure interactions with the review and tagging systems.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

## Getting Started
Follow these instructions to set up and run the Books API project.

## Prerequisites
Ensure the following are installed:
- **Python** >= 3.10
- **PostgreSQL**
- **Redis**

## Project Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheBeyonder237/FastAPI-CRUD.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd fastapi-beyond-CRUD/
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```

6. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

7. **Start the Celery worker** (Linux/Unix):
   ```bash
   sh runworker.sh
   ```

## Running the Application
To start the application:
```bash
fastapi dev src/
```

### Using Docker
Alternatively, run the application with Docker:
```bash
docker compose up -d
```

## Running Tests
To execute tests:
```bash
pytest
```

## Contributing
You are welcome to fork the repository and submit pull requests for improvements or fixes.

## Contact
For further questions or suggestions, reach out via email: [davidngoue@orizonne.net](mailto:davidngoue@orizonne.net)
