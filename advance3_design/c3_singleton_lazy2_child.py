"""
单例模式被继承的时候，子类和父类居然是同一个类？
"""
class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

class SingletonChild(SingletonClass):
    pass


singleton = SingletonClass()
child = SingletonChild()
print(child is singleton)  # True

singleton.singl_variable = "Singleton Variable"
print(child.singl_variable)
