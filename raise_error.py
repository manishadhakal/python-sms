# def sum(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError('this is type error please input valid type')
# print(sum('1','2'))

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('not implemented define function please define dog sound')


class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name)

    def sound(self):
        return 'bhow bhow'
class Cat(Animal):
    def __init__(self,name,bread):
        super().__init__(name)

doggy=Dog('khushi','jap')

print(doggy.name)
print(doggy.sound())



