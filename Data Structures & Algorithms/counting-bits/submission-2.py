class Solution:
    def countBits(self, n: int) -> List[int]:

        # O(nlogn) solution
        # def numberbits(n):
        #     count = 0

        #     while n > 0:
        #         count += n & 1
        #         n = n >> 1
        #     return count
        
        # output = []
        # for i in range(n + 1):
        #     output.append(numberbits(i))

        # return output

        # O(n)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + 1

        return dp
