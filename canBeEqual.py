class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        counter1={i:target.count(i) for i in target}
        counter2={j:arr.count(j) for j in arr}
        for i in counter1:
            try:
                dummy=counter2[i]
            except:
                return False
            if counter1[i]!=counter2[i]:
                return False
        return True
