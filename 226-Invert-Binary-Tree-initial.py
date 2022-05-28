# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Level-order traversal
        and swap them accordingly
        '''
        if not root:
            return root
        
        queue = deque()
        
        queue.append(root)
        
        while queue:
            cur_node = queue.popleft()
            
            if cur_node:
                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)
            # swap the left and right values
            
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
        
        return root
        