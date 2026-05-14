class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                value = seen[difference]
                if value and value != i:
                    return [min(i, value), max(i,value)]
        
        