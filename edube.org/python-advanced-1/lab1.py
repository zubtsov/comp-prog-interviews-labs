import random


class MobilePhone:
    def __init__(self, number: str):
        self.number = number

    def turn_on(self):
        return f'mobile phone {self.number} is turned on'

    def turn_off(self):
        return f'mobile phone is turned off'

    def call(self, number):
        return f'calling {number}'


if __name__ == '__main__':
    random.seed(1)

    mp1 = MobilePhone(random.randint(100000000, 999999999))
    mp2 = MobilePhone(random.randint(100000000, 999999999))

    print(mp1.turn_on())
    print(mp2.turn_on())

    print(mp1.call(random.randint(100000000, 999999999)))
    print(mp2.call(random.randint(100000000, 999999999)))

    print(mp1.turn_off())
    print(mp2.turn_off())
