class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp approach
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # m = dp[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        #     m = max(m, dp[i])
        
        # return m

        # greedy approach (space optimized)

        m = nums[0]

        cursum = 0

        for i in nums:
            if cursum < 0:
                cursum = 0
            cursum += i

            m = max(m, cursum)

        return m
        