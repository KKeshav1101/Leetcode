class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n=len(s)
        ans=0
        window=0
        left=0

        for right in range(n):
            window+=abs(ord(s[right])-ord(t[right]))
            while window>maxCost:
                window-=abs(ord(s[left])-ord(t[left]))
                left+=1
            ans=max(ans,right-left+1)
        return ans
