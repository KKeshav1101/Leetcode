class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans,c=[],Counter(candidates)
        def dfs(s,n,res):
            if s==target:
                return ans.append(res)
            if s>target or n<1:
                return
            for i in range(c[n]+1):
                dfs(s+i*n,n-1,res+[n]*i)
            
        dfs(0,50,[])
        return ans
