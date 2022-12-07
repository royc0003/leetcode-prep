# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        Note: this is an initial attempt; not an optimal solution
        '''

        totalSum = [0]

        def recursion(cur_node):
            # base case
            if not cur_node:
                return
            if cur_node.val >= low and cur_node.val <= high:
                totalSum[0] += cur_node.val
            recursion(cur_node.left)
            recursion(cur_node.right)            
            

        recursion(root)
        
        return totalSum[0]