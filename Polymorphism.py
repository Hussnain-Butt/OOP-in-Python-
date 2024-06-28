class Complex():
    def __init__(self, real, img):
      self.real = real
      self.img = img
    
    def showNum(self):
        print(self.real,"i +",self.img , "j ")
    
    # Addition 
    
    def __add__(self,num2):
     numReal = self.real + num2.real
     numImg =  self.img+ num2.img
     return Complex(numReal , numImg)
 
    # Substraction 
 
    def __sub__(self,num2):
      numReal = self.real - num2.real
      numImg =  self.img - num2.img
      return Complex(numReal , numImg)

num1 = Complex(4,8)    
num1.showNum()
num2 = Complex(7,9)
num2.showNum()

num3 = num1+num2
num3.showNum()

num4 = num1-num2
num4.showNum()
