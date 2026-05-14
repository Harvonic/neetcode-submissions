class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}

        l, r = 0, 0
        res = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxfreq = max(freq.values())
            windowl = r - l + 1

            if windowl - maxfreq <= k:
                res = max(res, windowl)
            else:
                freq[s[l]] -= 1
                l += 1
            
            r += 1
        
        return res
             


        

        