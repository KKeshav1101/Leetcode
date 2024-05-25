class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def permute_rec(nums,current_index,result):
            if current_index == len(nums)-1:
                result.append(list(nums))
                return
            for index in range(current_index,len(nums)):
                nums[current_index],nums[index]=nums[index],nums[current_index]
                permute_rec(nums,current_index+1,result)
                nums[current_index],nums[index]=nums[index],nums[current_index]

        permute_rec(nums,0,result)
        return result
