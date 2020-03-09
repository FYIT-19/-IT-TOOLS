#python program to perform addition
#of two complex numbers using binary
# + operator overloading

class complex:
    
    def __init__(self, a, b):
        self.a =  a
        self.b = b

    def __add__(self, other):
    #adding two objects
        return self.a + other.a , self.b + other.b

    def __str__(self):
        return self.a , self.b

    
#creating objects
    
ob1 = complex(1, 2)
ob2 = complex(2, 3)
ob3 = ob1 + ob2
print(ob3)
 
