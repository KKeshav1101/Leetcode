class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=4:
            return 0
        nums.sort()
        ans=nums[-1]-nums[0]
        for i in range(4):
            ans=min(ans,nums[-(4-i)]-nums[i])
        return ans
