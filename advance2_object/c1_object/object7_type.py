"""
类型注解，用于提示参数类型
python > 3.5
感觉没啥用。让代码看起来非常复杂
添加注解后，即使传入不符合类型的参数也不会报错

1. 变量注解
2. 函数形参注解、返回值注解
3. union注解
"""

# 1.变量注解
a: int = 10
pi: float = 3.14


class Person:
    pass


p: Person = Person()

my_list: list[int] = [1, 2, 3, 4, 5]
my_persons: list[Person] = [Person(), Person(), Person()]
my_tuple: tuple = (1, 2, 3)
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}

my_list.append('a')  # 传入不符合注解类型的也不会报错
print(my_list)


# 2. 函数注解
def func(data: int) -> float:
    return data * 10.2


# 3. union注解 (混合注解)

from typing import Union

# 表示这个list可以是str, 也可以是int
my_list: list[Union[str, int]] = [1, 2, 'a', 'b']


def func2(data: Union[int, float]) -> Union[int, float]:
    pass
