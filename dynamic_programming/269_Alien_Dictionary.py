class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        1st pass:
        check if it's lexicographically sorted
        (1) check if the len(s1) <= len(s2)
        (2) check for the first differing word to establish order after prefix. if ab|c ab|d, the prefix of both words are the same,
        therefore, the order is c -> d.
        
        2nd pass: (Topoogical sorting)
        topo sort
        '''
        graph = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            
            minOfWords = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minOfWords] == w2[:minOfWords]:
                return ""
            # start traversing from the min of length
            for j in range(minOfWords):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        topSort = []
        visited, seen = set(), set()
        def dfs(curLetter):
            if curLetter in seen:
                return False
            
            if curLetter in visited:
                return True
            
            
            res = False
            
            visited.add(curLetter)
            seen.add(curLetter)
            
            for neighbLetter in graph[curLetter]:
                res = dfs(neighbLetter)
                if not res: # cycle found
                    return False
                
            topSort.append(curLetter)
            seen.remove(curLetter)
            return True

        for curLetter in list(graph):
            if not dfs(curLetter):
                return ""
        
        topSort.reverse()
        return "".join(topSort)
            
        
                
        
        
        
        
        
        
        
        
        