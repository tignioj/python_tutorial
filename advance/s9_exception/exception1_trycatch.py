def exception1():
    try:
        a = 1 / 0
    except:
        print("抛出了异常，但是没有存到变量e里面，不知道是什么异常")


def exception2():
    try:
        a = 1 / 0
    except Exception as e:
        print("捕获了异常的基类", e)


def exception3():
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        print("捕获了更具体的异常", e)


def exception4():
    try:
        a = 1 / 0
    except IndexError as e:
        print("你捕获不到我的", e)
    else:
        print("try成功执行了，就会执行我")


def exception5():
    try:
        a = 1 / 1
    except IndexError as e:
        print("你捕获不到我的", e)
    else:
        print("try成功执行了，就会执行我")

def exception6():
    try:
        a = 1 / 0
    except IndexError as e:
        print("你捕获不到我的", e)
    else:
        print("try成功执行了，就会执行我")
    finally:
        print("这是我最后的挣扎")

def exception7():
    try:
        l = []
        b = l[5]
        a = 1/0
    except (IndexError, ZeroDivisionError) as e:
        print("多个异常", e)

if __name__ == '__main__':
    exception7()