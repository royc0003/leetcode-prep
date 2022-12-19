import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = collections.defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        seen = set()

        def dfs(cur_node):
            if cur_node == destination:
                return True

            seen.add(cur_node)

            res = False

            for neighb_node in graph[cur_node]:
                if neighb_node not in seen:
                    res = dfs(neighb_node)
                    if res:
                        break
            return res
        
        return dfs(source)