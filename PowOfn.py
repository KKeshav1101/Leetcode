class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n<0:
            return 1/(x*self.myPow(x,-n-1))
        elif n%2==0:
            a=self.myPow(x,n//2)
            return a*a
        return x*self.myPow(x,n-1)
