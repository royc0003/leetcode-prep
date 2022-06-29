class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        1. Create a pattern map -> e.g. hot -> *ot | h*t | ho*
        2. Run a bfs to find the shortest path -> taking note that the neighbours of the cur_word
        # are the those with similar patterns to cur_word
        '''
        
        # Handle edge case here
        if endWord not in wordList:
            return 0
        
        # Add begining word to wordlist
        wordList.append(beginWord)
        
        # Initialize defaultlist from collections
        pattern_map = defaultdict(list)
        
        # Creation of pattern map
        for word in wordList:
            for j in range(len(word)):
                # cat| 0, 1 ,2 ( would 2 go out of range?) [3:]
                # [c, a, *]
                pattern = word[:j] + "*" + word[j+1:]
                pattern_map[pattern].append(word)
        
        # Take note that dqueue and set, will split the word into individual char
        queue = deque([beginWord])
        visited = set([beginWord])
        
        total_dist = 1
        
        while queue:
            cur_len = len(queue)
            for i in range(cur_len):
                cur_word = queue.popleft()
                
                if cur_word == endWord:
                    return total_dist
                # check current pattern
                # Retrieve the neighbours of the current word to be appended to queue
                # Look for all patterns that matches current word
                for j in range(len(cur_word)):
                    pattern = cur_word[:j] + "*" + cur_word[j+1:]
                    # Notice: neighbours of cur_word are those that fit into the same pattern
                    neighbours = pattern_map[pattern]
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
            total_dist += 1
            
        return 0
            