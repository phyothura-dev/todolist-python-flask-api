# 📝 TodoList API — Flask Backend

Todo List mobile app အတွက် RESTful API backend။ Flask + MySQL + JWT Authentication + Docker ဖြင့် တည်ဆောက်ထားပါသည်။

## Tech Stack

- **Python 3.11** / **Flask**
- **MySQL 8.0** (SQLAlchemy ORM)
- **JWT** (Flask-JWT-Extended)
- **Docker** / Docker Compose

## Quick Start

```bash
# Docker ဖြင့် run ရန်
docker-compose up --build

# Local ဖြင့် run ရန်
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Environment Variables (`.env`)

```env
DATABASE_URL=mysql+pymysql://user:password@db:3306/tododb
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
