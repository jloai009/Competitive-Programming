# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root, min_allowed, max_allowed):
        if root:
            if min_allowed >= root.val or root.val >= max_allowed:
                return False
            l = self.helper(root.left, min_allowed, root.val)
            r = self.helper(root.right, root.val, max_allowed)
            return l and r
        else:
            return True
