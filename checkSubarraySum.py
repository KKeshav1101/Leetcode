class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainders_found={0:-1}
        curr_sum=0

        for i in range(len(nums)):
            curr_sum+=nums[i]
            remainder = curr_sum%k
            if remainder in remainders_found:
                if i-remainders_found[remainder]>=2:
                    return True
            else:
                remainders_found[remainder]=i
        return False
