#program to use property()

class property_fun_demo:
  
  def get_age(self):
    #function to get age
    
    print("Getter method called")
    return self._age
  
  def set_age(self,a):
    #function to set age
    
    print("Setter method called")
    self._age = a
    
  def del_age(self):
    del self._age
    
  age = property(get_age, set_age, del_age)
  
mark = property_fun_demo()
mark.age = 10
print(mark.age)
