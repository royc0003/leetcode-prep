"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_new_mappping = {}

        def dfs(cur_node):
            if cur_node in old_new_mappping:
                return old_new_mappping[cur_node]
            
            new_node = Node(cur_node.val)
            old_new_mappping[cur_node] = new_node

            for neighb_node in cur_node.neighbors:
                res = dfs(neighb_node)
                new_node.neighbors.append(res)
            
            return new_node
        return dfs(node) if node else None