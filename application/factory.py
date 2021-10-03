from flask import Flask
from application.api.moon import moon
from application.api.sun import sun


def create_app():
    app = Flask(__name__)
    app.register_blueprint(moon, url_prefix=moon.url_prefix)
    app.register_blueprint(sun, url_prefix=sun.url_prefix)

    return app
