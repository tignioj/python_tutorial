class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 两个下划线，表示私有成员变量
        self.__money = 100

    def __get_money(self):
        return self.__money

    def __str__(self):
        return f'name={self.name}, age={self.__age}, money={self.__get_money()}'


p = Person('张三', 20)
print(p.name)
# print(p.__age)  # 无法访问私有成员变量
# p.__money()  # 无法访问私有方法
print(p)
p.__money = 900  # 无法赋值，实际上相当于创建了一个名称为__money的变量，并不会影响私有成员变量的指
print(p)  # 仍然是100
print(p.__money)  # 访问的不是私有变量，而是我们自己赋值的
