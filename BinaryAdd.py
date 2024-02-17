#uses carry mod 2 to keep binary system intact, while adding digit by digit
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=""
        carry=0
        i=len(a)-1
        j=len(b)-1
        while(i>=0 and j>=0 or carry):
            if i>=0:
                carry+=int(a[i])
                i=i-1
            if j>=0:
                carry+=int(b[j])
                j=j-1
            s=str(carry%2)+s
            carry//=2
        return s
