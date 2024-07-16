# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def find(n,val,path):
            if n.val==val:
                return True
            if n.left and find(n.left,val,path):
                path+="L"
            elif n.right and find(n.right,val,path):
                path+="R"
            return path
        s,d = [],[]
        find(root,startValue,s)
        find(root,destValue,d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U"*len(s))+"".join(reversed(d))
