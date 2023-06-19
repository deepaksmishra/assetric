from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#from .base_model import Base
#from app import db
from app.config import Config

migrate = Migrate(compare_type = True)
ma = Marshmallow()
db = SQLAlchemy()

class Base(db.Model) :
    __abstract__ = True
    created_at = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp() , nullable = False )
    updated_at = db.Column(db.TIMESTAMP, server_default = db.func.current_timestamp() , nullable = False , onupdate = db.func.current_timestamp())


