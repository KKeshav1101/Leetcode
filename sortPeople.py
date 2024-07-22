class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n=len(names)
        d={}
        for index in range(n):
            d[heights[index]]=names[index]
        heights.sort(reverse=True)
        for index in range(n):
            h=heights[index]
            names[index]=d[h]
        return names
