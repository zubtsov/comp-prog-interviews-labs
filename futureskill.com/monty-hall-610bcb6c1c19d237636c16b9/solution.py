class Solution:
    def __init__(self, api):
        self.api = api
        self.round_number = -1

    def level_1_stay(self, revealed):
        import random

        if revealed == -1:
            self.chosen_door = random.randint(0, 2)

        return self.chosen_door

    def level_2_switch(self, revealed):
        import random

        if revealed == -1:
            self.chosen_door = random.randint(0, 2)
        else:
            result = [0, 1, 2]
            result.remove(self.chosen_door)
            result.remove(revealed)
            self.chosen_door = result[0]

        return self.chosen_door

    def level_3_monte_carlo(self, revealed):
        if revealed == -1:
            self.round_number += 1

        if self.round_number < 1000:
            return self.level_1_stay(revealed)
        else:
            return self.level_2_switch(revealed)
