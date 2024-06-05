class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=s.split(' ')
        ans=[]
        for i in lst:
            if i!='':
                ans.append(i)
        return ' '.join(ans[::-1])
