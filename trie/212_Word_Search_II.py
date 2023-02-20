class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_word = False
        self.ref_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_node = self.root
        cur_node.ref_count += 1
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
            cur_node.ref_count += 1
        cur_node.is_word = True

    def get_root(self):
        return self.root
    
    def prune(self, word):
        cur_node = self.root
        cur_node.ref_count -= 1
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
                cur_node.ref_count -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        # build the trie tree
        for word in words:
            trie.insert(word)
        
        ROW, COL = len(board), len(board[0])
        res = set()

        def dfs(r, c, cur_string, cur_node, i):
            # check if is within word
            if cur_node.is_word and cur_string not in res:
                res.add(cur_string)
                cur_node.is_word = False
                # peform pruning for matched word here; to reduce complexity
                trie.prune(cur_string)
            # ensure that we do not dfs() in the path that has already been pruned
            if r < 0 or r == ROW or c < 0 or c == COL or (r,c) in seen or board[r][c] not in cur_node.children or cur_node.children[board[r][c]].ref_count < 1:
                return
            
            # Backtracking applied here
            seen.add((r,c))
            dfs(r+1, c, cur_string + board[r][c], cur_node.children[board[r][c]], i+1)
            dfs(r-1, c, cur_string + board[r][c], cur_node.children[board[r][c]], i+1)
            dfs(r, c+1, cur_string + board[r][c], cur_node.children[board[r][c]], i+1)
            dfs(r, c-1, cur_string + board[r][c], cur_node.children[board[r][c]], i+1)
            seen.remove((r,c))

        cur_node = trie.get_root()
        for r in range(0, ROW):
            for c in range(0, COL):
                seen = set()
                dfs(r, c, "", cur_node, 0)
        return res