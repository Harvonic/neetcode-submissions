class Solution:
    def findMin(self, nums: List[int]) -> int:


        l, r = 0, len(nums) - 1
        smallest = nums[0]

        while l <= r:

            if (nums[l] <= nums[r]):
                smallest = min(smallest, nums[l])
                break
            
            mid = l + (r-l)//2

            # case 1: l and mid are sorted
            if (nums[l] <= nums[mid]):
                l = mid + 1
            else: # case 2: r and mid are sorted
                r = mid - 1
            
            
            smallest = min(smallest, nums[mid])


        
        return smallest



        