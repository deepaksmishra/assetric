from app.models.user import User
from app.models.base_model import db

class SignupHelper : 
    
    def registeruser(self,name, username , mobileno,whatsappno,email,password):
        try :
            create = User(name=name,mobileno = mobileno , password =password , email = email , whatsappno = whatsappno , username= username)
            db.session.add(create)
            db.session.commit()

        except Exception as e:
            print(e)
