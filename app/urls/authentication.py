from app.handler.authentication import UserHandler , LoginHandler , SignupHandler
from app import api



api.add_resource(LoginHandler,'/login')
api.add_resource(UserHandler,'/user')
api.add_resource(SignupHandler,'/signup')