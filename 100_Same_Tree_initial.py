# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        extremely verbose
        we can simplify the logic
        
        '''
        if not p and not q:
            return True
        
        stack =[(p,q)]
        
        while stack:
            p , q = stack.pop()
            # check for val
            if (p and q) and p.val != q.val:
                return False
            if (not p and q) or (p and not q):
                return False
            if (not p.left and q.left) or (p.left and not q.left) or (not p.right and q.right) or (p.right and not q.right):
                return False
            
            if p and q:
                if p.left and q.left:
                    stack.append([p.left, q.left])
                if p.right and q.right:
                    stack.append([p.right, q.right])
                    
                    
                    
        return True
            