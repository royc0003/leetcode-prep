# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        '''
        step 1: get all possible subTreeSum
        step 2: compute the biggest subTreeSum1 * subTreeSum2
        step 3: return the module of 1000000007
        '''
        maxPossibleSumArr = []
        def treeSum(cur_node):
            if not cur_node:
                return 0 
            leftTree = treeSum(cur_node.left)
            rightTree = treeSum(cur_node.right)
            subTreeSum = leftTree + cur_node.val + rightTree
            maxPossibleSumArr.append(subTreeSum)
            return subTreeSum
        
        totalSum = treeSum(root)
        res = float('-inf')
        for subTreeSum1 in maxPossibleSumArr:
            subTreeSum2 = totalSum - subTreeSum1
            res = max(res, subTreeSum1*subTreeSum2)
        return int(res) % 1000000007

