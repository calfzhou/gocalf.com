from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        def once_max(r: range) -> tuple[int, int, int]:
            """Extended maxProfit from 121-best-time-to-buy-and-sell-stock solution.
            Finds the max profit with at-most one transaction.
            Returns (max profit, best buy day, best sell day)
            """
            max_profit = 0
            buy = sell = -1
            min_price = inf
            min_price_day = -1
            for i in r:
                price = prices[i]
                if price <= min_price:
                    min_price = price
                    min_price_day = i
                if price - min_price > max_profit:
                    max_profit = price - min_price
                    buy = min_price_day
                    sell = i

            return max_profit, buy, sell

        profit, buy, sell = once_max(range(n))
        if profit == 0: return 0

        return profit + max(
            once_max(range(buy))[0],
            once_max(range(sell+1, n))[0],
            once_max(range(sell-1, buy, -1))[0]
        )
