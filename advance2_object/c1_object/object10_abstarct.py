"""
需要导入 abc.abstractmethod和继承abc.ABC
感觉python没必要弄抽象类。
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def bark(self):
        """
        不同动物叫声不一样
        :return:
        """



# an = Animal() # 抽象类不能实例化? Java可以匿名方式实例化

class Cat(Animal):
    def bark(self):
        print("cat bark")


class Dot(Animal):
    # 必须要实现抽象类方法才能实例化
    pass


Cat().bark()
Dot()  # 必须要实现抽象类方法才能实例化, 否则报错
