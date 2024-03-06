class Solution:
    def isPowerOfThree(self, n):
        if n < 3 and n != 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True
