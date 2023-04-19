class Solution:
    def __init__(self, api):
        self.api = api

    def level_1(self):
        self.api.place_plant('tree', 0)

    def level_2(self):
        self.api.place_plant('bush', 1)

    def level_3(self):
        self.api.place_plant('tree', 0)
        self.api.place_plant('tree', 1)
        self.api.place_plant('bush', 2)
        self.api.place_plant('tree', 3)
        self.api.place_plant('tree', 4)

    def level_4(self):
        self.api.place_hedge(['tree', 'tree', 'bush', 'tree', 'tree'])

    def level_5(self):
        self.api.place_hedge(['bush', 'bush', '', '', 'bush'])

    def level_6(self, hedge_directions):
        mapping = {1: 'tree', 2: 'bush', 0: ''}
        self.api.place_hedge(list(map(mapping.get, hedge_directions)))
