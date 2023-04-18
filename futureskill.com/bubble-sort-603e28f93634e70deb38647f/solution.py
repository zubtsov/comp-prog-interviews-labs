class Solution:
    def __init__(self, api):
        self.api = api

    def sort_the_list(self):
        swap_happened = True
        while swap_happened:
            swap_happened = False
            for i in range(1, self.api.size()):
                if not self.api.is_ordered(i - 1, i):
                    self.api.swap(i - 1, i)
                    swap_happened = True
