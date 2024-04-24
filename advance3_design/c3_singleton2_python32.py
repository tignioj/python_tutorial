from functools import lru_cache

@lru_cache(maxsize=None)
class CustomClass(object):

    def __init__(self, arg):
        print(f"CustomClass initialised with {arg}")
        self.arg = arg

c1 = CustomClass("foo")
c2 = CustomClass("foo")
c3 = CustomClass("bar")

print(c1 == c2)
print(c1 == c3)