class Student:
    name = None
    age = None

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    

s1 = Student()
s1.name = "张三"
s1.say_hello()
