class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        O(V+E)
        '''
        visited = set()
        bi_graph = defaultdict(list)
        
        for e1, e2 in edges:
            bi_graph[e1].append(e2)
            bi_graph[e2].append(e1)
        
        def dfs(source, prev):
            if source in visited:
                return False
            
            visited.add(source)
            for neighb_node in bi_graph[source]:
                if neighb_node == prev:
                    continue
                if not dfs(neighb_node, source):
                    return False
            
            return True
        
        
        return dfs(0, -1) and n == len(visited)
            
            
            
                    
            
        