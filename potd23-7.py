class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=Counter(nums)
        return sorted(nums,key=lambda x:(d[x],-x))
        
