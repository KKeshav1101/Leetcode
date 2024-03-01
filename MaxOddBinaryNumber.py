class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        no_of_ones=s.count('1')
        zeroes_count=len(s)-no_of_ones
        return "1"*(no_of_ones-1)+"0"*zeroes_count+"1"
            
