from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        i = 1
        while i < len(prices):
            current_profit = prices[i] - min_price
            if current_profit > max_profit:
                max_profit = current_profit
            elif prices[i] < min_price:
                min_price = prices[i]
            i += 1

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
