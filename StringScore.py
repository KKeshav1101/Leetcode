class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score=0
        for i in range(1,len(s)):
            score=score+abs(ord(s[i-1])-ord(s[i]))
        return score
