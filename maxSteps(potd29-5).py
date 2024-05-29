class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        value=0
        count=0
        for i in range(n):
            if int(s[i])==1:
                value=value+2**(n-i-1)
        while(value>=1):
            if(value==1):
                return count
            count=count+1
            if(value%2==0):
                value=value//2
            else:
                value=value+1
