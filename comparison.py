#python program to overload
#a comparison operators

class Num:
    
    def __init__(self,num):
        self.num = num

    def __gt__(self, num1):
        #Function compare & t return the greatest number
        
        if (self.num > num1.num):
            return True
        else:
            return False


#Object created
        
ob1 = Num(5)
ob2 = Num(3)
if (ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")




    
