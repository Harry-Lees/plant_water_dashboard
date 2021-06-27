from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .core.routes import blueprint as core_blueprint

    app.register_blueprint(core_blueprint)

    return app