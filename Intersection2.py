class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #to ensure space complexity is reduced
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)
        cnt=Counter(nums1) #creates a hash map with frequencies of each element
        ans=[]
        for x in nums2:
            if cnt[x]>0:
                ans.append(x)
                cnt[x]-=1
        return ans
