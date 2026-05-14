class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        matching = {}
        for word in strs:
            frequency = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                frequency[index] += 1
            t = tuple(frequency)
            if t in matching:
                matching[t].append(word)
            else:
                matching[t] = [word]
        
        return list(matching.values())
        