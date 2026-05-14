class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                dp[1] = 1
            if i == 2:
                dp[2] = 2
            if i >= 3:
                dp[i] = dp[i-1] + dp[i-2]
                
        return dp[n]



        