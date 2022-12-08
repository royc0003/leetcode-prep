# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        O(N) Complexity | O(N) Space
        '''
        
        def leaf(root):
            res = [] 
            stack = [root]
            while stack:
                cur_node = stack.pop() 
                if not cur_node.left and not cur_node.right:
                    res.append(cur_node.val)
                
                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)
            return res
        
        res_1 = leaf(root1)
        res_2 = leaf(root2)
        if len(res_1) != len(res_2):
            return False
        for i , val in enumerate(res_1):
            if val != res_2[i]:
                return False
        return True

