# TodoList Flask Backend Context

## Architecture
- Use Flask Application Factory: `create_app()` in `app/__init__.py`.
- Keep extension singletons in `app/extensions.py` and call `.init_app(app)` inside factory.
- Use Blueprint routing:
  - Auth: `app/routes/auth_routes.py` with `/api/auth`
  - Tasks: `app/routes/task_routes.py` with `/api/tasks`
- Keep business logic in `app/services/`; routes should stay thin.

## Data and Infra
- Stack: Python 3.11, Flask, SQLAlchemy, JWT, Flasgger (Swagger UI), Pgsql (Docker Compose).
- Models live in `app/models/` and import `db` from `app.extensions`.
- For schema/model changes, run migrations: `flask db migrate` then `flask db upgrade`.

## Implementation Conventions
- New routes: add Blueprint in `app/routes/` and register in `app/__init__.py`.
- New services: add in `app/services/` and call from routes.
- New config keys: add to `app/config.py` with `os.getenv()` and define in `.env`.
- New extensions: instantiate in `app/extensions.py`, initialize in factory.
- HTTP responses: use shared helpers in `app/response.py` (`success`, `fail`) from routes/controllers.
- Service contract: services in `app/services/` should focus on business logic and data access; return business objects/data, and let routes handle HTTP response formatting.
- API docs: keep Flasgger enabled at `/apidocs/` and keep Swagger specs in `app/docs/` modules (for example `app/docs/auth_docs.py`, `app/docs/task_docs.py`) instead of inline route dictionaries.
- Swagger usage: routes should reference docs via `@swag_from(...)` imports from `app/docs/*`.

## Workflow
- After API route changes, verify Swagger UI renders at `/apidocs/` and route specs match the latest payload format.
- Keep route handlers thin: parse request, call service, return `success(...)` in try block and `fail(...)` in except block.
- When response shape changes, update both `app/response.py` and all impacted Swagger doc modules in `app/docs/`.
- Keep service layer framework-light: avoid returning Flask response objects from services.
