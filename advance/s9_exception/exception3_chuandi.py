def fun1():
    a = 1 / 0


def fun2():
    print("fun2 start"), fun1(), print("fun2 end")


def hello():
    try:
        print("hello start")
        fun2()
        print("hello end")
    except Exception as e:  # Exception 是所有异常的基类
        print("捕获到异常",e)


hello()
