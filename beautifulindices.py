class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        a_indices=[i for i in range(len(s)-len(a)+1) if s[i:i+len(a)]==a]
        b_indices=[j for j in range(len(s)-len(b)+1) if s[j:j+len(b)]==b]
        beautiful_indices=[]
        i_ptr,j_ptr=0,0
        while i_ptr < len(a_indices) and j_ptr < len(b_indices):
            i,j=a_indices[i_ptr],b_indices[j_ptr]
            if abs(j-i)<=k:
                beautiful_indices.append(i)
                i_ptr+=1
            elif j<i-k:
                j_ptr+=1
            else:
                i_ptr+=1
        return beautiful_indices
