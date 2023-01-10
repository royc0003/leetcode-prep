# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # similar to same tree problem
        def check_nodes(cur_node,sub_node):
            if not cur_node and not sub_node:
                return True
            if not cur_node or not sub_node:
                return False
            if cur_node.val != sub_node.val:
                return False
            left_tree = check_nodes(cur_node.left, sub_node.left)
            right_tree = check_nodes(cur_node.right, sub_node.right)
            return left_tree and right_tree
        # iterative version 
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node:
                if cur_node.val == subRoot.val:
                    if check_nodes(cur_node, subRoot):
                        return True
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)
        return False