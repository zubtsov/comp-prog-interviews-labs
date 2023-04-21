class Solution:
    def __init__(self, api):
        self.api = api

    def get_buy_and_sell_days(self):
        num_days = self.api.get_num_days()
        prices = [self.api.get_price_on_day(day) for day in range(num_days)]

        best_buy_day = 0
        best_sell_day = 1
        best_delta = prices[best_sell_day] - prices[best_buy_day]

        for buy_day in range(num_days):
            for sell_day in range(buy_day + 1, num_days):
                current_delta = prices[sell_day] - prices[buy_day]
                if current_delta > best_delta:
                    best_delta = current_delta
                    best_buy_day = buy_day
                    best_sell_day = sell_day

        return [best_buy_day, best_sell_day]

    def get_buy_day(self):
        return self.get_buy_and_sell_days()[0]

    def get_sell_day(self):
        return self.get_buy_and_sell_days()[1]