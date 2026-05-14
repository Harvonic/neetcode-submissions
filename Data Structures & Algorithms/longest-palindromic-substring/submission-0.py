class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        length = 0
        left = 0
        right = 0

        for i in range(len(s)):
            
            # odd 
            l, r = i, i
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > length:
                    length = r - l + 1
                    left = l
                    right = r

                l -= 1
                r += 1

            #even
            l, r = i, i + 1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > length:
                    length = r - l + 1
                    left = l
                    right = r

                l -= 1
                r += 1
        
        return s[left:right+1]

        