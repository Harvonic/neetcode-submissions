class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in t:
            if i not in count:
                return False
            if count[i] - 1 < 0:
                return False
            count[i] -= 1
        
        # This can be replaced with just a check if the lengths are not equal
        # for i in s:
        #     if count[i] != 0:
        #         return False

        return True
        