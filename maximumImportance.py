class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        #find degree
        degree = [0]*n

        for road in roads:
            degree[road[0]]+=1
            degree[road[1]]+=1
        cities=list(range(n))
        cities.sort(key=lambda x: -degree[x])

        total_importance=0
        for i in range(n):
            total_importance+=(n-i)*degree[cities[i]]

        return total_importance
