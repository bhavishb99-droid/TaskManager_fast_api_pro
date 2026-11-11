# Task Manager API

A lightweight FastAPI-based task management service built with SQLite for local persistence. It includes CRUD operations for tasks and exposes interactive API documentation through Swagger UI.

## Features

- Create a task
- Get all tasks
- Get a single task by ID
- Update an existing task
- Delete a task
- SQLite database persistence
- Automatic API documentation via FastAPI Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
TASK_MANAGER/
├── main.py                  # FastAPI app entry point
├── routes/
│   └── tasks.py             # Task API endpoints
├── schema/
│   └── schemas.py           # Pydantic request models
├── service/
│   └── models.py            # SQLite task logic
├── database/
│   └── database.py          # Database connection and table creation
├── task.db                  # SQLite database file
├── .gitignore
└── README.md                # Project documentation
```

## Prerequisites

- Python 3.9+
- pip

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the Application

From the project root, start the server:

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Task Model

```json
{
  "title": "Complete project report",
  "description": "Finish the monthly task report and send it for review.",
  "priority": "High",
  "status": "Pending"
}
```

### Supported Priority Values

- Low
- Medium
- High

### Supported Status Values

- Pending
- In Progress
- Completed

## Example Request

Create a task:

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Write documentation",
    "description": "Create a README for the project",
    "priority": "Medium",
    "status": "Pending"
  }'
```

## Notes

- The app uses a local SQLite database file named `task.db`.
- The database tables are automatically created on application startup.
- FastAPI's Swagger UI provides easy testing for all endpoints without additional tooling.

## License

This project is provided as a learning/demo task management API.
