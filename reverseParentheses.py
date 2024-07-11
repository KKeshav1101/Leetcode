class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for char in s:
            if char==')':
                reverse=""
                while stack and stack[-1]!='(':
                    reverse+=stack.pop()
                if stack:
                    stack.pop()
                for c in reverse:
                    stack.append(c)
            else:
                stack.append(char)

        return ''.join(stack)
