# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        Time: O(N)
        Space: O(N)
        Bottom-up approach
        
        The idea:
        - if cur_node.val < low  ; we exceeded the lowest range and need to go bigger; therefore go rightwards
        - if cur_node.val > high: we have exceeded the highest range and need to go smaller; therfore leftwards
        - if not violation, we perform root.left + root.val + root.right
        '''
        
        def bottomUp(curNode):
            if not curNode:
                return 0 
            if curNode.val < low:
                return bottomUp(curNode.right)
            elif curNode.val > high:
                return bottomUp(curNode.left)
            else:
                return bottomUp(curNode.left) + curNode.val + bottomUp(curNode.right)
        
        return bottomUp(root)