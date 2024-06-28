# this is how to create a class

class Student:
    name="Hussnain"

# this is how to create an object
s1 = Student()
print(s1.name) 


# contructors

class Car:
    college = "ABC college Name"
    def __init__(self,name,color,model):
        self.name=name,
        self.color=color,
        self.model=model,
        print("Adding a new Detail in Database")
         
c1 = Car("Honda City","Black",2017)
print(c1.name)

# Practice quiz

class Student:
    def __init__(self, name, marks):
      self.name = name
      self.marks = marks
    @staticmethod  #Static Method
    def hello():
       print("hello")

    def get_avg (self):
       sum = 0
       for val in self.marks:
          sum  += val
        
       print(f"Hi {self.name} Your avg Score is: {sum/3}")

s1 = Student("Tony Starc",[99,78,120])
s1.hello()
s1.get_avg()