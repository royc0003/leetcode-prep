class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Kruskal's Algorithm -- minimum_spanning_tree + union_find
        Time Complexity: O (E*log(V)); but O(N)^2 to build the graph
        '''

        par = [point for point in range(0, len(points))]
        rank = [1] * len(points)
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        
        minHeap = [] 
        # create the graph; src to dest 
        for i in range(0, len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                weight = abs(x1 - x2) + abs(y1 - y2)
                minHeap.append([weight, i, j]) # weight, src, dst
        heapq.heapify(minHeap)
        
        mst = [] 
        cur_sum = 0 
        # stop when we reach maximm possible edges that nodes can be connected
        while len(mst) < len(points) - 1:
            min_node = heapq.heappop(minHeap)
            weight, src, dst = min_node[0], min_node[1], min_node[2]
            if not union(src, dst):
                continue
            cur_sum += weight
            mst.append([src,dst])
        
        return cur_sum