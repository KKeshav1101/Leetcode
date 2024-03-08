class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=[]
        for i in nums:
            c.append(nums.count(i))
        count=0
        m=max(c)
        for i in c:
            if(i==m):
                count+=1
        return count
