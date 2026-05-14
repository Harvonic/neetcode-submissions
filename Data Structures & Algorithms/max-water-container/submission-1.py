class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1

        highest = 0

        while l < r:
            height = min(heights[l], heights[r])
            distance = r - l

            highest = max(highest, height * distance)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return highest