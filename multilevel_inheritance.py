#program to demonstrate multilevel inheritance

class student:
    
    def _accept(self):
        #function to accept student details
        
        self._roll = input("Enter roll number:")
        self._class_ = input("Enter class:")
        self._div = input("Enter division:")
        self._semi = input("Enter semester:")


#Class derived from class student
        
class marks(student):
    
    def _semmarks(self):
        self._oop = int(input("Enter oop marks:"))                    
        self._pp = int(input("Enter pp marks:"))
        self._dm = int(input("Enter dm marks:"))
        self._dbms = int(input("Enter dbms marks:"))
        self._wp = int(input("Enter wp marks:"))                 
        self._it = int(input("Enter it marks:"))


#class derived from class marks
class result(marks):
    
    def semresult(self):
        self.total = self._oop + self._pp + self._dm + self._it + self._dbms + self._wp
        self.perc = self.total / 600 * 100
        print("total",self.total)
        print("percentage",self.perc)

        
a = result()
a._accept()                          
a._semmarks()
a.semresult()                          
