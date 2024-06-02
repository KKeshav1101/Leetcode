class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        c=0
        i=0
        while(i<n):
            while(i<n and s[i]==' ') :
                i+=1
            count=False
            while(i<n and s[i]!=' '):
                i+=1
                count=True
            if(count):c+=1
            i+=1
        return c   
