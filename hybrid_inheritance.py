#program to demonstrate hybrid inheritance

#parent class
class Parent:
     
     def func1(self):
         print("this is function one")


 #derived class from class parent
         
class Child(Parent):
     
     def func2(self):
         print("this is function 2")

 
class Child1(Parent):
     
     def func3(self):
         print(" this is function 3")


#derived class from class child & child1
class Child3(Child, Child1):
     def func4(self):
         print(" this is function 4")

 
ob = Child3()
ob.func2()
