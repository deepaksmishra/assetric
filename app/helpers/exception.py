

class AppExceptionHelper(Exception):
    def __init__(self,message,payload = {}):
        self.message = message
        self.payload =payload 
    def send_error_message(self):
        return {'status': 400, 'data': self.payload , 'error' : self.error}
    