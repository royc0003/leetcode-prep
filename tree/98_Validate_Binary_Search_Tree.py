# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        use lower and upper limits
        '''
        
        def validate(root, lowerLimit, upperLimit):
            if not root:
                return True
            if root.val >= upperLimit or root.val <= lowerLimit:
                return False
            
            leftTree = validate(root.left, lowerLimit, root.val)
            rightTree = validate(root.right, root.val, upperLimit)
            
            return leftTree and rightTree
        
        return validate(root, float('-inf'), float('inf'))
        
        