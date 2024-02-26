class Solution:
    def addBinary(self,a,b):
        s=bin(int(a,2)+int(b,2))
        return s[2::]
