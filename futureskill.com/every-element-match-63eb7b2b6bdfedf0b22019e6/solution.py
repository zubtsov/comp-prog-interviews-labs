class Solution:
    def __init__(self, api):
        self.api = api

    def every_element_match(self, list_length, value):
        for i in range(list_length):
            if self.api.get_element(i) != value:
                return False
        return True
