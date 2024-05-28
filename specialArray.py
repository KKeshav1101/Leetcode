class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        for i in range(n+1):
            count=sum([1 for num in nums if num>=i])
            if count==i:
                return i
        return -1
            
