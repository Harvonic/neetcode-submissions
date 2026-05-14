class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxLength = 0
        currLength = 0
        seen = {}

        l, r = 0, 0

        # while r < len(s):
        #     if s[r] not in seen:
        #         seen[s[r]] = True
        #     else:
        #         while (s[l] != s[r]):
        #             seen[s[l]] = None
        #             l += 1
        #         seen[s[l]] = None
        #         l += 1
        #     maxLength = max(maxLength, r - l + 1)
        #     r += 1

        # cleaner solution with keeping track of last seen index
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
            r += 1

        return maxLength
        