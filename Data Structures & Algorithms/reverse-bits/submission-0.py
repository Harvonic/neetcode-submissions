class Solution:
    def reverseBits(self, n: int) -> int:

        reversed = 0

        power = 31 
        while (n > 0):
            if n % 2 == 1:
                reversed += 2 ** power
            n = n // 2
            power -= 1
        
        return reversed



        