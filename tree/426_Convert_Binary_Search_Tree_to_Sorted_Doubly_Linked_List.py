"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Time Complexity: O(N)
        In-place
        '''
        if not root:
            return

        stack = []
        cur = root
        first, last = None, None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur_node_popped = stack.pop()
                if not first:
                    first = cur_node_popped
                else:
                    cur_node_popped.left = last
                    last.right = cur_node_popped
                    last = last.right
                last = cur_node_popped
                cur = cur_node_popped
                cur = cur.right
        last.right = first
        first.left = last
        return first