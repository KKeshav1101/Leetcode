class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        mapped_list = []
        for i,num in enumerate(nums):
            s=str(num)
            n=''.join(str(mapping[int(ch)]) for ch in s)
            mapped_list.append((num,int(n),i))

        mapped_list.sort(key=lambda x:(x[1],x[2]))

        sorted_nums = [t[0] for t in mapped_list]

        return sorted_nums
