class Bank:
  name = " "
  acctno = 0
  initial_bal = 5000
  amt = 0
  
  def accept(self):
    #This function accept details from user
    
       print("enter name,acctno and initial balance")
       self.name = input()
       self.acctno = int(input())
       self.initial_bal = float(input())
       print("Customer details")
       print(self.name)
       print(self.acctno)
       print(self.initial_bal)
       
  def deposit(self):
    #This function will calculate current value after deposited amount is added
    
    print("enter amount to be deposited")
    self.amt = int(input())
    self.initial_bal = self.initial_bal + self.amt
    print("updated balance is",self.initial_bal)

  def withdraw(self):
    #This function will calculate current value after withdrawn amount is subtracted

    print("Enter amount to be withdraw")
    self.amt = int(input())
    self.initial_bal = self.initial_bal - self.amt
    print("updated balance is ",self.initial_bal)

    
#Creating object to call the function
b1 = Bank()
b1.accept()
b1.deposit()
b1.withdraw()











    
