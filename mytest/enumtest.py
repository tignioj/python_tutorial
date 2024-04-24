# https://docs.python.org/zh-cn/3.7/library/enum.html#functional-api
from enum import Enum, Flag, auto

a1 = Enum('Animal', 'ANT BEE CAT DOG')
print(a1.ANT)
print(type(a1.ANT))


class Animal2(Enum):
    ANT = 1
    BEE = 2
    CAT = 3


class Animal3(Enum):
    ANT = 1
    BEE = 2
    CAT = 3


print(Animal2.ANT == Animal3.ANT)


class Color(Flag):
    BLACK = 0
    RED = auto()
    BLUE = auto()
    GREEN = auto()


print(Color.RED == Color.BLUE)
print(Color.RED)


# 自定义输出名称
class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class Color2(NoValue):
    RED = object()
    BLUE = object()
    GREEN = object()

print(Color2.RED)

class Color3(NoValue):
    RED = 'redd'
    BLUE = 'bluee'
    GREEN = 'greenn'

print(Color3.RED.value)
