class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count=defaultdict(int)
        print(count)
        for x in s:
            count[x]+=1
        for x in t:
            count[x]-=1
        for val in count.values():
            if (val!=0):
                return False
        return True
