class Solution:
    def countOfAtoms(self, s):
        def is_digit(c):
            return '0' <= c <= '9'
        
        def is_upper(c):
            return 'A' <= c <= 'Z'
        
        def is_lower(c):
            return 'a' <= c <= 'z'
        
        n = len(s)
        stk = []
        i = 0
        
        while i < n:
            if s[i] == '(':
                stk.append((s[i], 0))
                i += 1
            elif s[i] == ')':
                i += 1
                mul = 0
                while i < n and is_digit(s[i]):
                    mul = mul * 10 + int(s[i])
                    i += 1
                if mul == 0:
                    mul = 1
                
                temp = []
                while stk and stk[-1][0] != '(':
                    name, count = stk.pop()
                    count *= mul
                    temp.append((name, count))
                stk.pop()  # Remove '('
                
                for name, count in temp:
                    stk.append((name, count))
            else:
                if i + 1 < n and is_lower(s[i + 1]):
                    name = s[i] + s[i + 1]
                    i += 2
                else:
                    name = s[i]
                    i += 1
                
                count = 0
                while i < n and is_digit(s[i]):
                    count = count * 10 + int(s[i])
                    i += 1
                if count == 0:
                    count = 1
                
                stk.append((name, count))
        
        # Reconstruct the result
        mp = {}
        for name, count in stk:
            mp[name] = mp.get(name, 0) + count
        
        result = []
        for name, count in sorted(mp.items()):
            result.append(name)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)
