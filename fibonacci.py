class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        i = self.fib(n - 1)
        j = self.fib(n - 2)
        return i + j
