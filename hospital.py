import patient 
class Hospital(object):
    def __init__(self,hospName,capacity):
        self.patients=[]
        self.hospName=hospName
        self.capacity=capacity
        self.bedsInH=1
        print "Hospital Name:",self.hospName,"Capacity:",self.capacity
    def admit(self,p):
       
        if self.capacity >= 1:
                               
            p.bedNumber=self.bedsInH
            self.bedsInH+=1
            
            self.patients.append(p)
                                           
            self.capacity-=1 
            print "Name:",p.name
            print "Patient Admitted"
        else:
            print "Hospital is full cant receive patient:",self.patients[len(self.patients)-1].name
    def discharg(self,disPatName):
        for disPat in self.patients:
            if disPat.name == disPatName:
                print "Patient discharhed: ",disPatName
                self.patients.remove(disPat)
    def info(self):
        for piFile in self.patients:
            print "Name:",piFile.name,"/Alergies:",piFile.alergy,"/Bed Number:",piFile.bedNumber,"/Patient ID:",piFile.idd




pat1 = patient.Patient("ali","nothing")
pat2 = patient.Patient("naeif","fog")
pat3 = patient.Patient("nick","nothing")
hosp1=Hospital("alkindis",4)
hosp1.admit(pat1)
hosp1.admit(pat2)
hosp1.admit(pat3)
hosp1.discharg("ali")
hosp1.info()



    
    
        