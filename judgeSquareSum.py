import math as m
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left,right=0, int(math.sqrt(c))
        while left<=right:
            if left*left+right*right==c:
                return True
            elif left*left+right*right>c:
                right-=1
            else:
                left+=1
        return False
