"""
装饰器：实际上也是一种闭包，作用是在不破换目标函数原有功能下新增功能
"""

def sleep():
    import random, time
    print("睡眠中...")
    time.sleep(random.randint(1,5))

# sleep()
# 给函数新增功能：在调用sleep前增加输出"我要睡觉了"，调用睡眠后增加"我起床了"
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

# mysleep = outer(sleep)
# mysleep()

# 和下面的有啥不同？？上面的多了闭包。能看到有啥好处吗？似乎没有
def mysleep1(func):
    print("我要睡觉了")
    func()
    print("我起床了")
mysleep1(sleep)