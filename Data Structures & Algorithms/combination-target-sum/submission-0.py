class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        
        output = []

        def dfs(i, curr, total):
            if total == target:
                output.append(curr.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            val = nums[i]
            curr.append(val)
            dfs(i, curr, total + val)
            curr.pop()

            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return output
    


        