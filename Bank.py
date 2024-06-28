class Account():
    def __init__(self, bal, acc):
      self.bal = bal
      self.acc = acc
      
    def Debit(self,amount):
       self.bal -= amount
       print("Rs.",amount, "was Debited")
       print("Total Balance =:", self.get_balance())

    
    def Credit(self,amount):
       self.bal+=amount
       print("Rs.",amount, "was Credited")
       print("Total Balance =:", self.get_balance())


    def get_balance(self):
       return self.bal
       


acc1 = Account(10000,12345)
acc1.Debit(5000)
acc1.Credit(3000)