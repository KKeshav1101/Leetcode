class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay)<m*k:
            return -1
        left, right = 1,max(bloomDay)
        while left<right:
            mid = left + (right-left)//2
            if self.feasible(bloomDay,mid,m,k):
                right=mid
            else:
                left=mid+1
        return left

    def feasible(self,bloomDay,days,m,k):
        bonquets, flowers = 0,0
        for bloom in bloomDay:
            if bloom>days:
                flowers=0
            else:
                bonquets+=(flowers+1)//k
                flowers=(flowers+1)%k
        return bonquets>=m
