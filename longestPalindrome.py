class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cfreq = Counter(s)
        oddfreq = 0
        for frequency in cfreq.values():
            if frequency%2==1:
                oddfreq+=1
        if oddfreq > 1:
            return len(s)- oddfreq+1
        return len(s)
