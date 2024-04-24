class Animal:
    def speak(self): pass
class Dog(Animal):
    def speak(self): print("汪汪汪")
class Cat(Animal):
    def speak(self): print("喵喵喵")
def make_noise(animal: Animal):
    animal.speak()


make_noise(Dog())  # 汪汪汪
make_noise(Cat())  # 喵喵喵
