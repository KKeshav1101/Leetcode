class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        count=defaultdict(int)
        for i in s:
            count[i]=count[i]+1
        sortedcount=sorted(count.items(),key=lambda x:x[1], reverse=True)
        for char,freq in sortedcount:
            ans=ans+char*freq
        return ans
