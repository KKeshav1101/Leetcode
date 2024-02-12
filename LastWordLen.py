#length of last word in a string
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist=s.split()
        return len(slist[-1])
