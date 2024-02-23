class IntegerValue:

    def check_if_int(self, value):
        if type(value) != int:
            raise TypeError('Значение не целочисленное')
        
    def __set_name__(self, owner, name):
        self.name = '_' + name
        
    def __set__(self, instance, value):
        self.check_if_int(value)
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Coordinate:
    number = IntegerValue()

    def __init__(self, number):
        self.number = number


a = Coordinate(5)
print(a.__dict__, a.number)



