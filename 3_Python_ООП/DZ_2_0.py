class Descriptor:
    @staticmethod
    def validate_point(num):
        return num if type(num) == int else 0

    def __init__(self, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        setattr(instance, self.name, self.validate_point(value))
        # instance.__dict__[self.name] = value

    # def __set__(self, instance, value):
    #     setattr(instance, self.name, self.validate_point(value))

    # def __delete__(self, instance):
    #     del instance.__dict__[self.name]

class MyClass:
    my_attr = Descriptor('my_attr')

my_obj = MyClass()
my_obj.my_attr = input("?- "), input("?- "), input("?- ")

print(my_obj.my_attr)