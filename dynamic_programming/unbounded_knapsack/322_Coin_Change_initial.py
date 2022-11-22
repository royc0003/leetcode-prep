class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        KnapSack Unbounded problem -- because weight can be reepated multiple times
        #1 solve with brute force first;
        the amount can be treated like weight
                        0
                    /         \
        # need to keep track of weight + minimum number of coins
        
        Y-axis: Capacity
        X-Axis: item no.
        grid area = number of coins
        '''
        
        def unboundedKnapSack(i, currentAmount, totalCoins):
            # handle 2 base cases:
            # base case1: if we get the exact amount
            if currentAmount == 0:
                return 0
            
            # base case2: beyond boundary 
            if i == len(coins):
                return float('inf')
            
            # skip 
            totalCoins = unboundedKnapSack(i+1, currentAmount, totalCoins)
            
            currentAmount = currentAmount - coins[i]
            
            # don't skip
            if currentAmount >= 0:
                possibleCoins = 1 + unboundedKnapSack(i, currentAmount, totalCoins)
                
                totalCoins = min(totalCoins, possibleCoins) 
            
            return totalCoins
        res = unboundedKnapSack(0, amount, 0)
        
        return res if res != float('inf') else -1
                
                
        