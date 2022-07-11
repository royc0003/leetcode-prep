class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        # Create bi-directional graph
        bi_graph, visited = defaultdict(list), set()
        total_count = 0 
        for e1, e2 in edges:
            bi_graph[e1].append(e2)
            bi_graph[e2].append(e1)
        
        def dfs(node):
            if node in cycle:
                return False
            cycle.add(node)
            visited.add(node)
            
            for neighb_node in bi_graph[node]:
                dfs(neighb_node)
            
            return True
        
        for node in range(n):
            if node not in visited:
                cycle = set()
                dfs(node)
                total_count += 1
        return total_count
            
        