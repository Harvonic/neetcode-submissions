class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
           
            encoded += strs[i] + "\x1f"
        
        return encoded


    def decode(self, s: str) -> List[str]:

        decoded = []
        print(s)
        pointer = 0
        for c in range(len(s)):
            if s[c] == "\x1f":
                decoded.append(s[pointer:c])
                pointer = c + 1
        
        return decoded
