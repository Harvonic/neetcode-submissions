class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # seen = {}

        # for i in range(len(nums)):
        #     seen[nums[i]] = i
        
        # for i in range(len(nums)):
        #     difference = target - nums[i]

        #     if difference in seen and seen[difference] != i:
        #         return [i, seen[difference]]

        # one loop:

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        
        