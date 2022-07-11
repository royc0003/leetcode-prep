class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        CYCLE PREVENTION
        find-by-union (rank)
        Init, Par and Rank
        (1) Create a find() -> with path-compression()
        (2) Create a union
        '''
        par = [i for i in range(len(edges)+1)] # e.g 3 nodes = [0,1,2,3], where 1 = parent of itself
        rank = [1] * (len(edges)+1)
        
        # Find()
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]  # include path compression
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: # having the same parents == being in the same set, then perform cycle prevention
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
                
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        