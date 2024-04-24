"""
python类中的常用的魔术方法
__init__ 构造
__str__  相当于java的toString()
__it__
__le__
__eq__
还有其他自己查文档
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years'

    def __lt__(self, other):  # less than 我是否小于其他类
        return self.age < other.age

    def __le__(self, other):  # less equal <=
        return self.age <= other.age

    def __eq__(self, other): # equal
        return self.age == other.age and self.name == other.name

    def say_hello(self):
        print(self)


s1 = Student('zhangsan', 20)
s2 = Student('zhangsan', 20)
s3 = Student('lisi', 30)
print(s1 == s2)
print(s1 <= s2)
print(s3 > s2)
