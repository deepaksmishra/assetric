
from flask_restful import Resource
from flask import request
from app.handler.base_handler import BaseHandler
from app.helpers.authetication import SignupHelper
from app.config.sucess_config import sucess_config
from app.models.user import User
from app.config.error_config import error_config
from app.helpers.exception import AppExceptionHelper
    
class LoginHandler(BaseHandler):
    def post(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)

class UserHandler(BaseHandler):
    def get(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)

    def put(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)

    def post(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)


    def delete(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)


            

class SignupHandler(BaseHandler):
    def post(self):
        try:
            payload = request.get_json()
            name = payload.get('name')
            username = payload.get('username')
            mobileno = payload.get('mobileno')
            whatsappno = payload.get('whatsappno')
            email = payload.get('email')
            password = payload.get('password')
            user = User.query.filter_by(email=email).first()
            if user : 
                raise  AppExceptionHelper(error_config[0]) 
            SignupHelper.registeruser(self,name, username , mobileno,whatsappno,email,password)
            return self.return_json(status=200,data={},sucess=sucess_config[0])
        except AppExceptionHelper as error : 
            error = AppExceptionHelper.send_error_message(error)
            return self.return_json(status=error['status'],data=error['data'],error=error['error'])
        except Exception as e : 
            print(e)

        

    
