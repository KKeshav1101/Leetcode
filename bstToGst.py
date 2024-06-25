# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val=0
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.val+=node.val
            node.val=self.val
            dfs(node.left)

        dfs(root)
        return root
