class Solution:
    def __init__(self, api):
        self.api = api
        self.pets = {}

    def speak(self, name):
        return self.pets[name].cry()

    def add_pet(self, name, species):
        match species:
            case "cat":
                self.pets |= {name: Cat(name)}
            case "dog":
                self.pets |= {name: Dog(name)}
            case _:
                self.pets |= {name: Pet(name)}
        pass


class Pet:
    def __init__(self, name):
        self.name = name

    def cry(self):
        return "Hi!"


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def cry(self):
        return "Woof"


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def cry(self):
        return "Meow"
