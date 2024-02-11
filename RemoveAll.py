#program to remove all occuerences of a target, in place from a list
class Solution(object):
    def removeElement(self, nums, val):
        kount=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[kount]=nums[i]
                kount+=1
        print(kount)
        return kount
