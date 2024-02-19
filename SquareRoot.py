class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0 or x==1):
            return x
        i=1
        while(i<=x/i):
            if(x/i==i):
                print("here")
                return i
            i+=1
        return i-1
