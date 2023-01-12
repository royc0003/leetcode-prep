import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        dfs solution
        '''
        graph = collections.defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        seen = set()
        def dfs(cur_node, prev_node):
            if cur_node in seen:
                return False
   
            seen.add(cur_node)

            for neighb_node in graph[cur_node]:
                if neighb_node != prev_node:
                    res = dfs(neighb_node, cur_node)
                    if not res:
                        return False
            return True
        res = dfs(0, -1) 
        if len(seen) != n:
            return False

        return res