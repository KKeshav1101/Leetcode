class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        lsum=(n*(n+1))//2
        rsum=0
        while lsum>rsum:
            rsum+=n
            if rsum==lsum:
                return n
            lsum-=n
            n-=1
        return -1
