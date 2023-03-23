class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        Union Find
        O(E + V)
        '''

        if len(connections) < n - 1:
            return -1

        rank = [1] * n
        par = [i for i in range(0, n)]
        total_nodes = n -1
        def find(p):
            while p != par[p]:
                # path compression
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find (n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return True
        conflict_count = 0
        for e1, e2 in connections:
            if not union(e1, e2):
                conflict_count += 1
            else:
                # successful conneciton
                total_nodes -= 1
        return total_nodes