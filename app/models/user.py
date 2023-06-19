from .base_model import Base , db
from app.config import Config

class User(Base): 

    __tablename__ = Config.TABLE_PREFIX + 'user'
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String )
    username = db.Column(db.String )
    password = db.Column(db.String )
    email = db.Column(db.String )
    mobileno = db.Column(db.String )
    whatsappno = db.Column(db.String )


