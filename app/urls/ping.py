from app.handler.base_handler import Ping
from app import api
api.add_resource(Ping,'/ping')