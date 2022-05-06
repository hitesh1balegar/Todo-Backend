from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('gunicorn.error')
logger = custom_logger(logger)
cors = CORS()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mcqpaskeitvrxa:278f828a7da8310c770a3fd04e49cec4990759c96a0d061f883d027fb4a95268@ec2-34-194-73-236.compute-1.amazonaws.com:5432/d34kp88oa924l3'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

    from static.todoApp import todo_list
    app.register_blueprint(todo_list, url_prefix='/api/v1')

    return app
