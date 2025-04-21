# fastapi-mysql-app/fastapi-mysql-app/README.md

# FastAPI MySQL App

This project is a FastAPI application that serves as an intermediate between a MySQL remote database and a React frontend application. It allows parent users to register their children for courses through a secure API.

## Project Structure

```
fastapi-mysql-app
├── src
│   ├── auth
│   ├── database
│   ├── routers
│   ├── schemas
│   ├── config.py
│   └── main.py
├── .env
├── requirements.txt
├── alembic.ini
└── pyproject.toml
```

## Features

- Secure API accessible only by the frontend
- User authentication and registration
- Course management
- Student registration

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-mysql-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file.

5. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Access the API at `http://localhost:8000`. Use the provided endpoints for user registration, course management, and student registration.

## License

This project is licensed under the MIT License.