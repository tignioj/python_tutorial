"""
单例模式
"""
class Tool:
    pass
t1 = Tool()
t2 = Tool()
print(t1,t2)

# 如何实现单例？
# 非常简单，提前创建，然后让其它类导入
class StrTool:
    pass
# 饿汉模式，有没有懒汉模式？
strtool = StrTool()

# 然后让其他类导入即可