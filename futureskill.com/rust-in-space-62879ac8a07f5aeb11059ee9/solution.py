class Solution:
    def __init__(self, api):
        self.api = api

    def level_2_say_hello(self):
        return 'Hello World'

    def level_3_process_input(self, input_value):
        return input_value[::-1]

    def level_4_use_the_api(self, x, y):
        self.api.set_destination(x, y)
