class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves=0
        nxt=nums[0]+1
        for i in range(1,len(nums)):
            if nxt>=nums[i]:
                moves+=nxt-nums[i]
                nxt+=1
            else:
                nxt=nums[i]+1
        return moves
