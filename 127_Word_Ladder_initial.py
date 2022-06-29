class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        edge case, check that the endWord is in the wordList before we continue
        
        Step 1: Create graph out of the words
        
        *ot -> {hot, dot, lot}
        h*t -> {hot}
        ho* -> {hot, }
        
        *og -> {dog, log, cog}
        d*g -> {dog}
        do* -> {dot, dog}a
        
        O(N*M)
        
        Step 2: Use grpah-bfs to perform the traversal
        
        '''
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)  
        pattern_map = defaultdict(set)
        
        for word in wordList:
            # ['h', 'o', 't']
            char_in_word = list(word)
            i = 0
            while i < len(char_in_word):
                tmp_split_word = list(word)
                # peform mutation on the reference word
                tmp_split_word[i] = "*"
                ref_word = ''.join(tmp_split_word)
                # print(ref_word)
                j = 0
                while j < len(wordList):
                    # perform mutation on the search word
                    search_word = list(wordList[j])
                    tmp_search_word = search_word
                    tmp_search_word[i] = "*"
                    # e.g. if *ot, hot == cot
                    tmp_search_word = ''.join(tmp_search_word)
                    if ref_word == tmp_search_word:
                        # Build the graph here
                        pattern_map[wordList[j]].add(word)
                        pattern_map[word].add(wordList[j])
                    j+= 1
                i += 1
        
        # Run BFS here
        queue, visited = deque(), set()
        queue.append(beginWord)
        visited.add(beginWord)
        total_length = 0
        while queue:
            cur_word = queue.popleft()
            
            for neighb_word in pattern_map[cur_word]:
                if neighb_word not in visited:
                    if neighb_word == endWord:
                        return total_length
                    queue.append(neighb_word)
                    visited.add(neighb_word)
            total_length += 1
            

            
        
            
                

            
            
                
                    
                    
                

        