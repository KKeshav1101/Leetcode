#check if power of 2 or not
import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        b=bin(n)
        s=str(b)
        if(s.count('1')>1):
            return False
        else:
            return True    
            
