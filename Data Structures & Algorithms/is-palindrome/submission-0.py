class Solution:
    def isPalindrome(self, s: str) -> bool:


        # clean the string
        sCleaned = ""

        for i in s:
            if i.isalnum() and i != " ":
                sCleaned += i.lower()
        l, r = 0, len(sCleaned) - 1

        print(sCleaned)
        
        while l < r:
            if sCleaned[l] != sCleaned[r]:
                return False
            l += 1
            r -= 1


        return True
        