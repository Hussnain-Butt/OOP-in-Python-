# Abstraction

class Car():
    def __init__(self):
      self.acc = False
      self.clutch = False
    def start(self):
         self.acc = True
         self.clutch = True
         print("Car Started....")

c1 = Car()
c1.start()

