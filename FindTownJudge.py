'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusts_c=[0]*(n+1)
        trusted_by_C=[0]*(n+1)
        for a,b in trust:
            trusts_c[a]+=1
            trusted_by_C[b]+=1
        for i in range(1,n+1):
            if(trusts_c[i]==0 and trusted_by_C[i]==n-1):
                return i
        return -1
