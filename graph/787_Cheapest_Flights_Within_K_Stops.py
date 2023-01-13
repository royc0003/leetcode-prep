import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Djikstra algo
        '''
        graph = collections.defaultdict(list)
        for flight in flights:
            source, dest, weight = flight[0], flight[1], flight[2]
            graph[source].append([weight, dest])
        visit = [0] * n
        min_heap = []
        heapq.heappush(min_heap, [0, src, k+1]) # <cur_weight, src, steps>
        while min_heap:
            cur_weight, cur_node, cur_k = heapq.heappop(min_heap)
            if cur_node == dst:
                return cur_weight
            if visit[cur_node] >= cur_k:
                continue
            visit[cur_node] = cur_k
            # relaxation technique d[u] + c[u, v] < d [v]
            for neighb_weight, neighb_node in graph[cur_node]:
                heapq.heappush(min_heap, [cur_weight+neighb_weight, neighb_node, cur_k-1])
        return -1