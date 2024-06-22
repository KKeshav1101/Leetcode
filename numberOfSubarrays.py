class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ansCount=0
        count=0
        i=0
        j=0
        while(j<len(nums)):
            if nums[j]%2!=0:
                k-=1
                count=0
            while k==0:
                if nums[i]%2!=0:
                    k+=1
                count+=1
                i+=1
            ansCount+=count
            j+=1
        return ansCount

                

        
