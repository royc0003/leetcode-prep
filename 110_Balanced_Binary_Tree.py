class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Recurisve Solution
        Start with an array [true/false, height]
        Recursively work upwards
        Check if abs (left - right) > 1
        If > 1, make sure to make array[False, height]
        Else: return 1 + max(left, right)
        '''
        
        def dfs(root):
            '''
            Pass value from bottom to top approach
            '''
            if not root:
                # where True refers to balanced, and 0 is the height
                return [True, 0]
            # dfs recursive method (Guides direction of DFS)
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Useful technique here:
            # Combining various checks together
            # checks if left is true/false, right is true/false, and if (left - right) <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]