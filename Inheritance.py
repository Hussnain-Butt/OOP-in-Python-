# parrent class

class Car:
    def __init__(self, type):
      self.type = type
      
      
    @staticmethod
    def start():
     print("Car Started....")

    @staticmethod
    def stop():
     print("Car Stop....")

# child class
class ToyotaCar(Car):
  def __init__(self, brand,type):
    super().__init__(type)
    self.brand = brand
    super().start()
    

c1 = ToyotaCar("Fortuner","Electric")

print(c1.type)


# class Methods

class Person():
    name="Hussnain"
    @classmethod
    def changename(cls):
     cls.name = "Rahul"

p1 = Person()
p1.changename()
print(Person.name)

