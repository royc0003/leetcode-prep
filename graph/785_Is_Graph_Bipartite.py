class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color_seen = {}

        def dfs(cur_node):
            for neighb_node in graph[cur_node]:
                if neighb_node in color_seen:
                    if color_seen[cur_node] == color_seen[neighb_node]:
                        return False
                else:
                    color_seen[neighb_node] = 1 - color_seen[cur_node]
                    if not dfs(neighb_node):
                        return False
            return True
        
        for node in range(0, len(graph)):
            if node in color_seen:
                continue
            color_seen[node] = 0
            if not dfs(node):
                return False
        return True