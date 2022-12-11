# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]

        def dfs(cur_node):
            if not cur_node:
                return 0 
            
            leftSubTree = dfs(cur_node.left)
            rightSubTree = dfs(cur_node.right)
            leftSum = max(0, leftSubTree)
            rightSum = max(0, rightSubTree)
            # without splitting
            res[0] = max(res[0], cur_node.val + leftSum + rightSum)

            # with splitting, we need to know return one of the paths back to the parent node
            return cur_node.val + max(leftSum, rightSum)
        
        dfs(root)
        return res[0]

        