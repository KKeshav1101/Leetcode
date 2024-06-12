class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for x in nums: freq[x]+=1
        count=0
        for x in range(3):
            nums[count:count+freq[x]] = [x]*freq[x]
            count+= freq[x]
