# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        prev = None
        stack = [root]
        # pre-order traversal
        while stack:
            cur_node = stack.pop()
            if cur_node:
                stack.append(cur_node.right)
                stack.append(cur_node.left)
                if prev:
                    prev.right = cur_node
                    prev.left = None
                    prev = prev.right
                prev = cur_node