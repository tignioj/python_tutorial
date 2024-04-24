def user_info(*args):
    print(args)


def user_info2(**kwargs):
    """
    传入类型必须是 k=v形式
    :param kwargs:
    :return:
    """
    print(kwargs)


def user_info3(*args, **kwargs):
    print('args:',*args)
    print('kwargs:',kwargs)


if __name__ == '__main__':
    user_info('name', 'zhangsan', 'age', 20)
    user_info2(name='zhangsan', age=20)
    user_info3('name','zhangsan', 'age', 20, name='lisi', age=30)
