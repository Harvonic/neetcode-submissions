class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
            
        dp = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1


        for i in range(amount + 1):
            for coin in coins:
                target = i - coin

                if target > 0:
                    dp[i] = min(dp[i], 1 + dp[target])

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


        