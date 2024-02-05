#first unique character in string
class Solution(object):
    def firstUniqChar(self, s):
        mp={}
        for i in s:
            mp[i]=mp.get(i,0)+1
        for i in range(len(s)):
            if(mp[s[i]]==1):
                return i
        return -1
