class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for word in strs:
            sortWord = "".join(sorted(word))
            ans[sortWord].append(word)
        
        return [v for i,v in ans.items()]
        
        
        