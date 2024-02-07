#checkforpalindrome in a number
class Solution(object):
    def isPalindrome(self, x):
        str_no=str(x)
        if(str_no==str_no[::-1]):
            return True
        else:
            return False        
