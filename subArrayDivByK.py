class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        l=[0 for i in range(k)]
        l[0]+=1
        count=0
        curr_sum=0
        for i in range(n):
            curr_sum = (curr_sum+nums[i]%k+k)%k
            count += l[curr_sum]
            l[curr_sum]+=1
        return count
