class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        O(N^2) solution
        (1) we know that if n-edge = n-vertices => cycle is formed.
        (2) when building a bi-direcitional graph:
            - if the same edges (e1, e2) are shown, it means that the potential of a loop is very high
            - check for reachability before building the graph, because if a node is not reachable, then it's not a disconnected graph.
                - and if it's reachable, return (e1, e2) because a cycle is formed.
        
        '''
        graph = defaultdict(list)
        
        def dfs(source, target):
            # base case
            if source in seen:
                return False
            if source == target:
                return True
            
            seen.add(source)
            
            for neighb_node in graph[source]:
                if dfs(neighb_node, target):
                    return True
            
            return False 
        
        # build the graph
        for e1, e2 in edges:
            seen = set()
            if e1 in graph and e2 in graph and dfs(e1, e2):
                return [e1, e2]
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        