class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        # while n > 0:
        #     if n % 2 == 1:
        #         count += 1
        #     n = n // 2

        # alternative using bit shift
        # while n > 0:
        #     if n % 2 == 1:
        #         count += 1
        #     n = n >> 1

        # smarter math using logical and
        while n > 0:
            count += n & 1
            n = n >> 1
        
        return count
        