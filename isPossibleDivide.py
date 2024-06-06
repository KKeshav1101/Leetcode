class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
                
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        
        while d:
            x = min(d)
            for i in range(x,x+k):
                if i not in d:
                    return False
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
        return True
