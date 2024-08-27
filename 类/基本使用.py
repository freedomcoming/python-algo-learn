


class Person(object):
    name = "unknow"
    def __init__(self) -> None:
        self.__age = 18


    @property
    def age(self):
        return self.__age



    @age.setter
    def age(self, data):
        print("age setter")
        self.__age = data

    
    @staticmethod
    def static():
        return "static method"
    
    @classmethod
    def cm(cls):
        return "class method"

p  = Person()

print(p.age)

p.age = 19

print(p.age)


print(p.static(), Person.static())

print(p.cm(), Person.cm())