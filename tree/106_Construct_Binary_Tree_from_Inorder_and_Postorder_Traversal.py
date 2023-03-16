# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        postorder = [9,15,7,20,3]
        inorder = [9,3,15,20,7]
        [9]     [15,20,7]
                [15] [7]

        Use postorder as the mid point of `in-order` to split left and right sub0tree
        '''
        def dfs(in_order_arr):
            if len(in_order_arr) < 1:
                return None
            cur_val = postorder.pop()
            node = TreeNode(cur_val)
            for i, val in enumerate(in_order_arr):
                if val == cur_val:
                    node.right = dfs(in_order_arr[i+1:])
                    node.left = dfs(in_order_arr[0:i])
            return node
        
        return dfs(inorder)
            
