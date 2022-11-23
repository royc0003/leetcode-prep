class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        res = 0 
        graph = defaultdict(list) # {origin: [<dest, weight>]}
        # Step 1: build the graph
        for time in times:
            origin, dest, weight = time
            graph[origin].append([dest,weight])
        
        # Step 2: initiliaze the minHeap
        # <weight, dest_node>
        heapq.heappush(minHeap, [0,k])
        
        visited = set()
        while minHeap:
            cur_weight, cur_node = heapq.heappop(minHeap)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            res = max(cur_weight, res)
            
            # similar to relaxation
            for neighb_item in graph[cur_node]:
                dest, weight = neighb_item
                if dest not in visited:
                    heapq.heappush(minHeap, [cur_weight + weight, dest])
        return res if len(visited) == n else -1
            
        
            
        
        
        