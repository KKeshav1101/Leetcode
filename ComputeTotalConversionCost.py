class Solution:
    CHAR_COUNT = 26
    INF = float('inf')

    def minimumCost(self, source, target, original, changed, cost):
        conversionGraph = self.buildConversionGraph(original, changed, cost)
        self.optimizeConversionPaths(conversionGraph)
        return self.computeTotalConversionCost(source, target, conversionGraph)

    def buildConversionGraph(self, original, changed, cost):
        graph = [[self.INF] * self.CHAR_COUNT for _ in range(self.CHAR_COUNT)]
        for i in range(self.CHAR_COUNT):
            graph[i][i] = 0
        for i in range(len(cost)):
            fromChar = ord(original[i]) - ord('a')
            toChar = ord(changed[i]) - ord('a')
            graph[fromChar][toChar] = min(graph[fromChar][toChar], cost[i])
        return graph

    def optimizeConversionPaths(self, graph):
        for k in range(self.CHAR_COUNT):
            for i in range(self.CHAR_COUNT):
                if graph[i][k] < self.INF:
                    for j in range(self.CHAR_COUNT):
                        if graph[k][j] < self.INF:
                            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    def computeTotalConversionCost(self, source, target, graph):
        totalCost = 0
        for i in range(len(source)):
            sourceChar = ord(source[i]) - ord('a')
            targetChar = ord(target[i]) - ord('a')
            if sourceChar != targetChar:
                if graph[sourceChar][targetChar] == self.INF:
                    return -1
                totalCost += graph[sourceChar][targetChar]
        return totalCost
