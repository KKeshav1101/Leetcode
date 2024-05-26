class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        if(x>0 and x<=2**31-1):
            while(x>0):
                res=10*res+x%10
                x=x//10
        elif(x<0 and x>=-2**31):
            x=-x
            while(x>0):
                res=10*res+x%10
                x=x//10
            res=res-2*res
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res
