from typing import List


class Solution:
    """
        TC: O(mn), m = amount, n = len(coins)
        SC: O(m)
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [0] * (amount + 1)
        vis = [False] * (amount + 1)

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if vis[amount]:
                return d[amount]
            vis[amount] = True

            ans = 1e5
            for i in range(len(coins)):
                sub = dp(amount - coins[i])
                if sub == -1:
                    continue
                ans = min(ans, sub + 1)

            d[amount] = ans if ans != 1e5 else -1
            return d[amount]

        return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [amount + 1] * (amount + 1)
        d[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    d[i] = min(d[i], d[i - coins[j]] + 1)

        return d[amount] if d[amount] != (amount + 1) else -1
