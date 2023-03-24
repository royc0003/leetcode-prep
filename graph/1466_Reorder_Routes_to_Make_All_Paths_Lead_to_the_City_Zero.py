class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        direction_graph = collections.defaultdict(set)
        bi_direction_graph = collections.defaultdict(list)

        for e1, e2 in connections:
            direction_graph[e1].add(e2)
            bi_direction_graph[e1].append(e2)
            bi_direction_graph[e2].append(e1)
        seen = set()
        total_count = [0]
        def dfs(cur_node):
            seen.add(cur_node)
            for neighb_node in bi_direction_graph[cur_node]:
                if neighb_node not in seen:
                    # check if is moving in forward direction
                    if neighb_node in direction_graph[cur_node]:
                        total_count[0] += 1
                    dfs(neighb_node)
        dfs(0)
        return total_count[0]