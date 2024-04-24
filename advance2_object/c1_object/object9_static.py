class Monster:
    name = 'zhangsan'
    age = 20

    def hi(self):
        print(f"name={self.name}, age={self.age}")

    @staticmethod
    def hello(name):
        print(f"Hello, {name}")


print(Monster.name)  # 类本身也是一个对象
Monster.hi(Monster)  # 把类对象作为self
m = Monster()
m.hi()
m.hello('zhangsan')
Monster.hello('lisi')