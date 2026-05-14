class Solution:
    def countBits(self, n: int) -> List[int]:

        def numberbits(n):
            count = 0

            while n > 0:
                count += n & 1
                n = n >> 1
            return count
        
        output = []
        for i in range(n + 1):
            output.append(numberbits(i))

        return output