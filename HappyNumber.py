class Solution(object):
    def isHappy(self, n):
        def isFinish(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            m = 0
            while n != 0:
                r = n % 10
                m += r * r
                n = n // 10
            return isFinish(m, seen)
        
        return isFinish(n, set())
