class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1={}
        for i in nums:
            dict1[i]=nums.count(i)
        print(dict1)
        result=[]
        for i in nums:
            if(dict1[i]==1):
                result.append(i)
        return result
