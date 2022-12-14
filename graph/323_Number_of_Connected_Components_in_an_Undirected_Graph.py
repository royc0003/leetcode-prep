import collections
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        
        dfs solution O(N) solution with seen set. 
        """
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set() #global seen set
        def dfs(cur_node):
            if cur_node in seen:
                return
            seen.add(cur_node)

            for neighb_node in graph[cur_node]:
                dfs(neighb_node)
        res = 0 
        for cur_node in range(0,n):
            if cur_node not in seen:
                dfs(cur_node)
                res += 1
        return res