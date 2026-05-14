class Solution:
    def isPalindrome(self, s: str) -> bool:


        # clean the string
        # sCleaned = ""

        # for i in s:
        #     if i.isalnum() and i != " ":
        #         sCleaned += i.lower()
        # l, r = 0, len(sCleaned) - 1
        
        # while l < r:
        #     if sCleaned[l] != sCleaned[r]:
        #         return False
        #     l += 1
        #     r -= 1


        # return True

        # optimal solution without filtering
        l, r = 0, len(s) - 1

        while l < r:

            # check if its alnum
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True