class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        cmax=-999999999
        csum=0
        for i in range(n):
            csum=csum+nums[i]
            cmax=max(csum,cmax)
            if(csum<0):
                csum=0
        return cmax
