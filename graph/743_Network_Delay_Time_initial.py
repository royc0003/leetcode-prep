class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Djikstra's algorithm
        (1) Initialize all to be infinite except the last 
        2-D Matrix
        (2) Select shortest path
        (3) For every neighboring nodes, perform relaxation technique
        
        Releaxation Technique: Important
        if d[u] + c(u,v ) < d[v]:
            d[v] = d[u] + c(u,v)
            
        1 --> 2 
        '''
        graph = defaultdict(list) # {origin: [<dest, weight>]}
        for time in times:
            origin, dest, weight = time
            graph[origin].append([dest, weight])
        
        nodesWeight = [float('inf')] * (n + 1)
        
        # first initialization
        nodesWeight[k] = 0
        seen = set()
        queue = deque()
        # initialize first val
        if k in graph:
            queue.append(k)
        
        res = -1
        while queue:
            cur_node = queue.pop()
            seen.add(cur_node)
            res = cur_node
            
            # perform relaxation steps for every neigh nodes
            next_smallest_node = float('inf')
            for neighb_node in graph[cur_node]:
                dest, weight = neighb_node
                # perform relaxation here
                if nodesWeight[cur_node] + weight < nodesWeight[dest]:
                    nodesWeight[dest] = nodesWeight[cur_node] + weight
                # greedy get only if the selected node is
                next_smallest_node = dest if dest not in seen and nodesWeight[dest] <= next_smallest_node else next_smallest_node
            
            # check for the smallest item seen so far
            if next_smallest_node != float('inf'):
                queue.append(next_smallest_node)
        
        return nodesWeight[res] if res != -1 else -1
        
            
            
            
            
            
        
        