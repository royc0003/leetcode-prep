# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        '''
        Naive Solution:
        - pass down nodes where it's the maximum
        - pass dow nodes where it's the minimum
        - and find the difference throughout
        O(N) solution
        '''
        maxDiff = float('-inf')
        stack = [[root, root.val, root.val]]
        while stack:
            cur_node, maxVal, minVal = stack.pop()
            
            if cur_node.val > maxVal:
                maxVal = cur_node.val
            if cur_node.val < minVal:
                minVal = cur_node.val

            diff = abs(maxVal - minVal)
            maxDiff = max(diff, maxDiff)

            if cur_node.right:
                stack.append([cur_node.right, maxVal, minVal])
            if cur_node.left:
                stack.append([cur_node.left, maxVal, minVal])

        return int(maxDiff)
