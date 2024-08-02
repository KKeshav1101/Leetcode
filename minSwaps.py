class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_ones = sum(nums)

        if total_ones == 0 or total_ones ==n:
            return 0
        
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones

        for i in range(n):
            current_ones -= nums[i]
            current_ones += nums[(i+total_ones)%n]
            max_ones=max(max_ones,current_ones)
        
        return total_ones - max_ones
