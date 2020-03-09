#program to demonstrate composition
class Salary:
    
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        #function to calculate the salary of the year
        return (self.pay * 12)
 
 
class Employee:
    
    def __init__(self, pay, bonus):
        
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
 
    def annual_salary(self):
        return "Total : " + str(self.obj_salary.get_total() + self.bonus)
 
 
obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
 
