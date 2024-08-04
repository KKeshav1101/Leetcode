class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        array=[]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                array.append(s)
        array.sort()
        mod=10**9+7
        return sum(array[left-1:right])%mod
