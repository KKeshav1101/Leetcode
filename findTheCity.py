class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Set the distance from a city to itself to 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate initial distances from the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Apply the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Determine the number of reachable cities within the distance threshold for each city
        reachable_cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_cities[i] += 1
        
        # Find the city with the smallest number of reachable cities
        min_reachable = float('inf')
        result_city = -1
        for i in range(n):
            if reachable_cities[i] <= min_reachable:
                if reachable_cities[i] < min_reachable or i > result_city:
                    min_reachable = reachable_cities[i]
                    result_city = i
        
        return result_city
