
import uuid
class Patient(object):
    def __init__(self,name,alergy):
        uniId=str(uuid.uuid4())
        uniId=uniId[-6:]
        self.idd=uniId
        self.name=name
        self.alergy=alergy
        self.bedNumber=""
                
