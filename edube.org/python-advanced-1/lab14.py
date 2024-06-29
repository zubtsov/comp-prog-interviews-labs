# https://edube.org/learn/python-advanced-1/metaprogramming-lab-metaclasses

from datetime import datetime


class InstantiationTime(type):
    instantiated_classes = set()

    def __new__(cls, name, bases, dictionary):
        dictionary['instantiation_time'] = datetime.now()
        dictionary['get_instantiation_time'] = lambda: dictionary['instantiation_time']
        cls.instantiated_classes.add(name)
        return super().__new__(cls, name, bases, dictionary)


if __name__ == '__main__':
    class MyClass(metaclass=InstantiationTime):
        pass


    class MyClass2(metaclass=InstantiationTime):
        pass


    mc1 = MyClass()
    mc2 = MyClass2()

    print(MyClass.get_instantiation_time())
    print(MyClass2.get_instantiation_time())
    print(InstantiationTime.instantiated_classes)
