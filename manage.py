from pathlib import Path
import time

from flask.cli import FlaskGroup
from flask_migrate import upgrade
from sqlalchemy import text

from app import create_app
from app.extensions import db

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("migrate")
def migrate_command():
    """Apply pending migrations; fallback to create_all on first run."""
    with app.app_context():
        max_retries = 30
        for attempt in range(1, max_retries + 1):
            try:
                db.session.execute(text("SELECT 1"))
                break
            except Exception as exc:  # noqa: BLE001
                if attempt == max_retries:
                    raise RuntimeError("Database is not reachable for migration.") from exc
                print(f"Waiting for database... ({attempt}/{max_retries})")
                time.sleep(2)

        migrations_env = Path("migrations/env.py")
        if migrations_env.exists():
            try:
                upgrade()
                print("Database migration completed with Alembic.")
            except ImportError as exc:
                print(f"Alembic migration skipped: {exc}")
                db.create_all()
                print("Fallback applied: tables created with db.create_all().")
        else:
            db.create_all()
            print("No valid Alembic setup found. Tables created with db.create_all().")


if __name__ == "__main__":
    cli()
