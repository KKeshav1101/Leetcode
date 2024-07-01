class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        state=0
        for i in arr:
            if i%2==0:
                state=0
            elif i%2!=0:
                state+=1
            if state==3:
                return True
        return False
