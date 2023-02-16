class Trie:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Trie()
            cur_node = cur_node.children[c]
        cur_node.is_word = True
    
    def dfs(self, cur_word_i, cur_node, word):
        # base-case:
        if cur_word_i >= len(word):
            return cur_node.is_word
        if word[cur_word_i] != '.' and word[cur_word_i] not in cur_node.children:
            return False
        res = False
        if word[cur_word_i] != '.':
            res = self.dfs(cur_word_i+1, cur_node.children[word[cur_word_i]], word)
        else:
            # run a dfs() on each of the cur_node of children
            for next_node in cur_node.children.values():
                res = self.dfs(cur_word_i+1, next_node, word)
                if res: break
        return res
        
        
    def search(self, word: str) -> bool:
        cur_node = self.root
        return self.dfs(0, cur_node, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)