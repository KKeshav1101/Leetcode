#remove duplicates from a sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        nums[:]=unique[:]
        k=len(nums)
        return k
