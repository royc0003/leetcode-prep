# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p, q = root, root

        def checkSymmetric(l, r):
            if (not l and not r):
                return True
            if not l or not r:
                return False 
            left_sub_tree = checkSymmetric(l.left, r.right)
            right_sub_tree = checkSymmetric(l.right, r.left)
            return l.val == r.val and left_sub_tree and right_sub_tree
        return checkSymmetric(p,q)