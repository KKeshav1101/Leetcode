class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset=set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
