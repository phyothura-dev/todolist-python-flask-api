# 📝 TodoList API — Flask Backend

Todo List mobile app အတွက် RESTful API backend။ Flask + PostgreSQL + JWT Authentication + Docker ဖြင့် တည်ဆောက်ထားပါသည်။

## Tech Stack

- **Python 3.11** / **Flask**
- **PostgreSQL 16** (SQLAlchemy ORM)
- **JWT** (Flask-JWT-Extended)
- **Flasgger** (Swagger UI for API docs)
- **Docker** / Docker Compose

## Quick Start

```bash
# With Docker
docker-compose up --build

# With Local
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Database Migration

```bash
# With Local
python manage.py migrate
# With Docker
docker compose exec web python manage.py migrate
```

## Environment Variables (`.env`)

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/todo_db
JWT_SECRET_KEY=your_super_secret_key
```

## API Endpoints

| Method   | Endpoint             | Description         |
| -------- | -------------------- | ------------------- |
| `POST`   | `/api/auth/register` | User registration   |
| `POST`   | `/api/auth/login`    | Login (returns JWT) |
| `POST`   | `/api/tasks/`        | Create task         |
| `GET`    | `/api/tasks/`        | List all tasks      |
| `PUT`    | `/api/tasks/<id>`    | Update task         |
| `DELETE` | `/api/tasks/<id>`    | Delete task         |

## API Documentation (Swagger UI)

Run the server and open:

- `http://localhost:5000/apidocs/` (Swagger UI)
- `http://localhost:5000/apispec_1.json` (OpenAPI spec JSON)

For protected task endpoints, click **Authorize** and set:

```text
Bearer <your_jwt_token>
```

## Project Structure

```
python/
├── app/
│   ├── __init__.py        # App factory
│   ├── config.py          # Configuration
│   ├── extensions.py      # DB, Migrate, JWT
│   ├── models/            # SQLAlchemy models
│   ├── routes/            # Blueprint routes
│   └── services/          # Business logic
├── migrations/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── .env
```
