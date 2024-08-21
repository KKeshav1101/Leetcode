class Solution:
    def strangePrinter(self, s: str) -> int:
        s = next(zip(*groupby(s)))

        @cache
        def f(i, j):
            if i > j:
                return 0

            res = 1 + f(i+1, j)
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    res = min(res, f(i, k-1) + f(k+1, j))

            return res

        return f(0, len(s)-1)
