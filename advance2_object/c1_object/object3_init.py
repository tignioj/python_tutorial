class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    

s1 = Student('zhangsan',20)
s1.say_hello()
