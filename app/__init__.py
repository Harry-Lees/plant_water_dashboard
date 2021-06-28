from flask import Flask

from .extensions import database

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .core.routes import blueprint as core_blueprint

    app.register_blueprint(core_blueprint)

    database.init_app(app)

    with app.app_context():
        database.create_all()

    return app