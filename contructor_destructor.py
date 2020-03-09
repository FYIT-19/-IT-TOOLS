#program to initialize the object and destroy

class person:

  def __init__(self,fname,lname):
    #Constructor
    
    print("Creates  and initialize of instance of person class")
    self.fname=fname
    self.lname=lname

  def getfullname(self):
          print(self.fname," ",self.lname)

  def __del__(self):
    #destructor
    
    print("Object has been destroyed")
  

P1=person("Siddhi","Shirke")
P1.getfullname()
P2=person("Riya","James")
P2.getfullname()
P1.__del__()
P2.__del__()         
