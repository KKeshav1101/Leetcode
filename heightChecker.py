class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h=heights[::]
        h.sort()
        count=0
        for i in range(len(heights)):
            if(heights[i]!=h[i]):
                count+=1
        return count
