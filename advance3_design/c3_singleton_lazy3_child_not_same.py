"""
单例模式被继承的时候，子类和父类居然是同一个类？
修改他们为不同的类
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


class BorgSingleton(object):
    _shared_borg_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj


borg = BorgSingleton()
borg.shared_variable = "Shared Variable"


class ChildBorg(BorgSingleton):
    pass


childBorg = ChildBorg()
print(childBorg is borg)
print(childBorg.shared_variable)