from email import message
from pickletools import read_bytes1
from flask_restful import Resource
from flask import request


class BaseHandler(Resource): 

    def __init__(self) :
        self.request = request
        self.page_no = 1
        self.page_size = 20

    def return_json(self,status = 200,data = {},error = {},sucess = {},header = {}):
        status_identifier = status//10**2%10
        try:
            if header and status_identifier == 2:
                return {"sucess":True,
                        "message":sucess['message'],
                        "data":data,

                        },status,header
            elif status_identifier == 2:
                return {"sucess":True,
                        "message":sucess['message'],
                        "data":data,

                        },status
            else : 
                return {"sucess":False,
                        "message":error['error_message'],
                        "error_code" : error['error_code'],
                        "data":data,

                        },status,header
        except Exception as e : 
            print(e)
    

class Ping(BaseHandler):
    def get(self):
        try:
            data = {}
            data['message']="assetric is working"
            return self.return_json(status=200,data=data,sucess=data)
        except Exception as e : 
            print(e)



            


        

    
