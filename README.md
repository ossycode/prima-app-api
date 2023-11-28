# prima-app-api

==============
Python-based API server for managing user data

# Installation

1. Install the dependencies via PIP. (If you use virtualenv you'll want to
   create a virtual environment and activate it first.)

   python -m venv your_venv_name # To Create a new virtual environment

   source your_venv_name/bin/activate # To Activate the virtual environment on (macOS/Linux)

   your_venv_name\Scripts\activate # To activate the virtual environment (Windows)

   pip install -r requirements.txt # Install project dependencies

# Start Server

Run `python manage.py runserver`

Browser API endpoint documentation is on `http://127.0.0.1:8000/api/docs/`

# API Endpoints

| #   | Request Method | Endpoint                                | Description                  | Param        | Example Request Body                                                                            | Response Format                 | Example Result                                                                         |
| --- | -------------- | --------------------------------------- | ---------------------------- | ------------ | ----------------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------- |
| 1   | GET            | `http://127.0.0.1:8000/api/users/`      | Retrieve all users           | None         | None                                                                                            | - HTTP status code: 200 OK      | `[ { "id": 0, "email": "user@example.com", "username": "string", "name": "string" } ]` |
| 2   | POST           | `http://127.0.0.1:8000/api/users/`      | Create a new user            | None         | `{ "email": "user@example.com", "username": "string", "password": "string", "name": "string" }` | - HTTP status code: 201 CREATED | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 3   | GET            | `http://127.0.0.1:8000/api/users/{id}/` | Retrieve a single user by ID | id (integer) | None                                                                                            | - HTTP status code: 200 OK      | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 4   | PATCH          | `http://127.0.0.1:8000/api/users/{id}/` | Update a user by ID          | id (integer) | `{ "email": "user@example.com", "username": "string", "password": "string", "name": "string" }` | - HTTP status code: 200 OK      | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 5   | DELETE         | `http://127.0.0.1:8000/api/users/{id}/` | Delete a user by ID          | id (integer) | None                                                                                            | - HTTP status code: 204         | No response body                                                                       |
