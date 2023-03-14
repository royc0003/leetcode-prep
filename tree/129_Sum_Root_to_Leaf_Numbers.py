# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Iterative Approach:: o(N)

        res = []
        stack = [[root, 0]]
        while stack:
            cur_node, cur_val = stack.pop()
            potential_val = cur_val * 10 + cur_node.val
            if not cur_node.left and not cur_node.right:
                res.append(potential_val)
            if cur_node.right:
                stack.append([cur_node.right, potential_val])
            if cur_node.left:
                stack.append([cur_node.left, potential_val])
        return sum(res)