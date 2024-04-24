def say_hello():
    print("hello")
    return None


def tuple1():
    a = (100, ['a'])
    # a[0] = 10 # 无法对元组赋值
    print(a[1])
    a[1][0] = 'b'
    print(a[1])  # 可以对元素赋值


def str1():
    mystr = "hello world, this is str1"
    print(mystr.index("world"))


def slilce1():
    """
    实际上取切片的时候，默认步长是1
    :return:
    """
    my_list = [0, 1, 2, 3, 4, 5, 6]
    print(my_list[:]) # 取全部
    print(my_list[-4])  # 取倒数第4
    print(my_list[1:4])  # 取下标1~4
    print(my_list[1:-4])  # 取下标1 ~ 倒数第4
    print(my_list[:4])  # 取0~4
    print(my_list[-4:-1])

def slice2():
    """
    [起始:结束:步长]
    指定步长写法 ::2
    :return:
    """
    mystr= "0123456"
    print(mystr[::2])  # ::2 表示设置步长为2
    print(mystr[::3])  # ::2 表示设置步长为3
    print(mystr[0:3:2])  # 取下标0~3，步长为2
    print(mystr[::-1])  # 等同于反转序列

def set1():
    a = set()  # 无序,不可重复
    a.add(1)
    a.add(2)
    a.add('hello')
    a.add('hello')
    a.add('world')
    a.add('test')
    a.add('你好')
    print(a)

if __name__ == '__main__':
    # str1()
    # slilce1()
    # slice2()
    set1()
