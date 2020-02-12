class protected:
    
    #protected data member
    _name = None
    _roll = None
    _branch = None

    
    def __init__(self,name,roll,branch):
         #Contructor
        self._name = name
        self._roll = roll
        self._branch = branch
        
    def _display_roll_and_branch(self):    #protected member function
            #accesing protected data members
            print("Roll:",self._roll)
            print("Branch:",self._branch)
            

class student(protected): #derived class
    
    def __init__(self,name,roll,branch):
         #constructor
        protected(self,name,roll,branch)
        
    def display(self):
        #function to display 
        print("Name:",self._name)
        self._displayrollAndbranch()
        

#creating object to call function
obj = student("Amit",120,"Information")
print("Name:",obj._name)
obj.display()
