class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Perform union find
        '''
        if len(edges) != n - 1: return False

        par = [i for i in range(0, n)]
        rank = [1] * n
        
        def find(p):
            # include path compression
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # cycle found
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for e1, e2 in edges:
            if not union(e1, e2):
                return False
        return True