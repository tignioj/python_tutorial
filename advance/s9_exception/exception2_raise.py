def fun1():
    raise Exception("主动抛出异常")


class CustomException(Exception):
    pass


def fun2():
    raise CustomException("自定义异常")


if __name__ == '__main__':
    try:
        fun2()
    except CustomException as e:
        print(f"异常信息:{e},类型:{type(e)}")
