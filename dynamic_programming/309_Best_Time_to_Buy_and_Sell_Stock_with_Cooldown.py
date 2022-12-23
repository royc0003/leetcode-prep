class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        knapsack 0 / 1 problem
        top-down approach with cache
        '''
        cache = {}
        def knapsack(i, isBuying, cache):
            if i >= len(prices):
                return 0
            if (i, isBuying) in cache:
                return cache[(i, isBuying)]
            
            cooldown = knapsack(i+1, isBuying, cache)

            if isBuying:
                buy = knapsack(i+1, not isBuying, cache) - prices[i]
                cache[(i, isBuying)] = max (buy, cooldown)
                
            else:
                sell = knapsack(i+2, not isBuying, cache) + prices[i]
                cache[(i, isBuying)] = max(sell, cooldown)

            return cache[(i, isBuying)]

        return knapsack(0, True, cache)