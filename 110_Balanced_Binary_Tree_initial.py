# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Recurisve Solution
        Notice that this is by passing value from top to bottom

        Correction to make although it still runs:
        - cur_node.left = dfs(cur_node.left)
        should be:
        left = dfs(cur_node.left)

        '''
        if not root:
            return True
        res = [1]
        
        def dfs(cur_node, height):
            # return the leaf_node height
            if not cur_node:
                return 0
            
            
            # get the left val
            cur_node.left = dfs(cur_node.left, height + 1)
            # get the right val
            cur_node.right = dfs(cur_node.right, height + 1)
            max_left = max(cur_node.left, height)
            max_right = max(cur_node.right, height)
            # compare between left and right subtree
            if abs(max_left - max_right) > 1:
                res[0] = 0
            return max(max_left, max_right)
        
        
        dfs(root, 0) 
        return True if res[0] else False
        
        
        
        