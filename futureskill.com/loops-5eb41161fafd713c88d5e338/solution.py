class Solution:
    def __init__(self, api):
        self.api = api

    def level_1(self):
        self.api.eat_bone(0)

    def level_2(self):
        self.api.eat_bone(0)
        self.api.eat_bone(1)
        self.api.eat_bone(2)

    def level_3(self):
        for i in range(18):
            self.api.eat_bone(i)

    def level_4(self):
        for i in range(22):
            if self.api.is_brown_bone(i):
                self.api.eat_bone(i)

    def level_5(self):
        for i in range(10):
            if i in [2, 4, 5]:
                continue
            self.api.eat_bone(i)

    def level_6(self):
        for i in range(10):
            if self.api.is_time_for_break():
                break
            self.api.eat_bone(i)

    def level_7(self):
        for dog_number in range(6):
            for bone_number in self.api.get_bones_for_dog(dog_number):
                self.api.eat_bone_for_dog(dog_number, bone_number)
