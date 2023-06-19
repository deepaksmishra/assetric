from flask import Flask
from flask import Blueprint
from flask_restful import Api
#from app.models import 
from app.config import Config
from app.models.base_model import db , ma , migrate


flask_app = Flask(__name__,instance_relative_config=True)
flask_app.config.from_object(Config)
api_bp = Blueprint('api',__name__)
api = Api(api_bp)
flask_app.register_blueprint(api_bp , url_prefix = '/api')

db.init_app(flask_app)
ma.init_app(flask_app)
migrate.init_app(flask_app , db)
from app import urls
