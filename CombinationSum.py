class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp=[[] for _ in range(target+1)]
        dp[0].append([])
        for i in range(1,target+1):
            for candidate in candidates:
                if candidate<=i:
                    for prev in dp[i-candidate]:
                        temp=prev+[candidate]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target]
