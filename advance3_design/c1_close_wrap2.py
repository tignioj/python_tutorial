"""
闭包：解决全局变量可能被修改的风险
使用nonlocal关键字可以使得内部函数持续访问外部函数的局部变量

优点：
1.无需定义全局变量就可以通过函数持续访问、修改某个指
2. 闭包使用的变量的所在函数内，不容易被错误的修改（相比于全局变量更安全）

缺点：由于内部函数持续引用外部函数的值，会导致内存无法释放
"""


# def outer(sum_val):
#     def inner(val):
#         sum_val += val # sum_val 未定义
#         print(f"sum={sum_val}")
#
#     return inner
#
# cal = outer(0)
# cal(20)
# cal(20)


def outer1(sum):
    def inner(val):
        nonlocal sum  # 使得sum可以修改
        sum += val
        print(f"sum={sum}")

    return inner


# cal1 = outer1(0)
# cal1(20)
# cal1(20)

num1 = 10

def outer3(num1):
    def inner(num2):
        nonlocal num1  # 访问的是num1而不是全局变量
        num1 += num2
        print(num1)

    return inner


cal3 = outer3(100)
cal3(1)  # 101
cal3(1)  # 102
print(num1)  # 全局变量未被修改
