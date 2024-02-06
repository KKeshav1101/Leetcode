#finding the first duplicate in a string
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict1={}
        for i in s:
            if i in dict1:
                return i
            dict1[i]=0
            dict1[i]=dict1[i]+1
