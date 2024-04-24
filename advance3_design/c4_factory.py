"""
工厂模式
"""


class Person:
    pass


class Worker(Person):
    pass


class Manager(Person):
    pass


class Student(Worker):
    pass


class Factory:
    @staticmethod
    def get_person(p_type):
        if p_type == 'manager':
            return Manager()
        elif p_type == 'student':
            return Student()
        elif p_type == 'workder':
            return Worker()


# 工厂模式的好处是统一接口，易于修改
stu = Factory.get_person('student')
