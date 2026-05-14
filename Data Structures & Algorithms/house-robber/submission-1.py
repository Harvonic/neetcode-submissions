class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        amt = dp[0] if dp[0] > dp[1] else dp[1]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max([dp[j] for j in range(0, i - 1)])
            amt = max(amt, dp[i])
        
        return amt


        