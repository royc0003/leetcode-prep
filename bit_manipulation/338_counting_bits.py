class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        dynamic programming solution
        0 --> 0
        1 --> 1  [msb]
        2 --> 10 [msb]
        3 --> 11 
        4 --> 100 [msb]
        curPower = 
        '''
        dp = [0] * (n+1)
        i, curPower = 0, 0
        while i < len(dp):
            if curPower*2 == i or curPower == 0 :
                curPower = i
            dp[i] = 1 + dp[i - curPower] if curPower != 0 else 0
            i += 1
        return dp
                
            
        
        