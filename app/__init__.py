from flask import Flask, jsonify
from .extensions import db, migrate, jwt, swagger, cors
from .routes.auth_routes import auth_bp
from .routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    swagger.init_app(app)
    cors.init_app(
        app,
        resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"].split(",")}},
        supports_credentials=False,
    )

    @app.get("/")
    def root():
        return jsonify(
            {
                "message": "TodoList API is running",
                "docs": "/apidocs/",
            }
        )

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app
