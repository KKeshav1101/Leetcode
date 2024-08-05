class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counter=Counter(arr)
        for v in arr:
            if counter[v]==1:
                k-=1
                if k==0:
                    return v
        return ''
