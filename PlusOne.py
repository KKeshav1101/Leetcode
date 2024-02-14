class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        if digits[-1]==9:
            carry=1
            for i in range(n-1,-1,-1):
                digits[i]+=carry
                carry=digits[i]//10
                digits[i]%=10

                if not carry:
                    break
            if carry:
                digits.insert(0,carry)
        else:
            digits[-1]+=1
        return digits
