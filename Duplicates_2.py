class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]]-i)<=k:
                    return True
            d[nums[i]]=i
        return False
