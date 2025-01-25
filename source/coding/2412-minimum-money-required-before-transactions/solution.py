class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        max2 = lambda a, b: a if a >= b else b
        max_cashback = 0
        max_cost = 0
        lost = 0
        for cost, cashback in transactions:
            if cashback < cost:
                lost += cost - cashback
                max_cashback = max2(max_cashback, cashback)
            else:
                max_cost = max2(max_cost, cost)

        return lost + max2(max_cashback, max_cost)
