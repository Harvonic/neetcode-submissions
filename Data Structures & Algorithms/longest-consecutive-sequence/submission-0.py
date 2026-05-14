class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        in_nums = {}
        start = []
        m = 0

        for i in nums:
            in_nums[i] = True
        
        for i in nums:
            if not (i - 1 in in_nums):
                start.append(i)
        
        for i in start:
            curr = 1
            while(i + curr in in_nums):
                curr += 1
            m = max(m, curr)



        return m
        