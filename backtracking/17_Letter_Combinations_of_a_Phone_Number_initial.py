class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
        mappedNumbers = { '2': ['a','b','c'],
                        '3': ['d','e','f'],
                        '4': ['g','h','i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m','n','o'],
                        '7': ['p','q','r','s'],
                        '8': ['t','u','v'],
                        '9': ['w','x','y','z']}
        # building the global variables. 
        # (1) usedList will be a boolean Array
        # (2) selectionList will be flattened possible results
        usedList, selectionList = [], []
        res = []
        
        for char in digits:
            curArray = mappedNumbers[char]
            usedList.append([False]*len(curArray))
            selectionList.append(curArray)
        
        def permute(depth, path, selectedList):
            # basecase
            if len(digits) == len(path):
                res.append(''.join(path[0::])) # deep-copy
                return
            
            for i in range(len(selectedList)):
                # check if has been used before
                if usedList[depth][i]:
                    continue
                # update usedList to used
                usedList[depth][i] = True
                # add to path
                path.append(selectedList[i])
                # permute
                permute(depth+1, path, selectionList[depth+1] if depth+1 < len(selectionList) else [] )
                # unselect and `un-used`
                path.pop()
                usedList[depth][i] = False
                
        permute(0, [], selectionList[0])
        
        return res
                
                
        
        
        
        