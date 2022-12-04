class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        '''
        O(N) complexity
        O(N) space solution
        '''
        indexMap = {}
        
        for i, char in enumerate(keyboard):
            indexMap[char] = i
        
        prevChar = keyboard[0]
        totalSum = 0 
        for char in word:
            prevCharIndex = indexMap[prevChar]
            curCharIndex = indexMap[char]
            
            totalSum += abs(curCharIndex - prevCharIndex)
            prevChar = char
        return totalSum
            
            
        
        