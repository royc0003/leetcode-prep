class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {} 
        def top_down(i, cur_amount):
            if cur_amount == amount:
                return 0 
            if i >= len(coins):
                # max
                return float('inf')
            if (i, cur_amount) in cache:
                return cache[(i,cur_amount)]
            # skip
            skip = top_down(i+1, cur_amount)
            # dont skip
            potential_amount = cur_amount + coins[i]
            dont_skip = float('inf')
            if potential_amount <= amount:
                res = top_down(i, potential_amount)
                if res != float('inf'):
                    dont_skip = 1 + res
            cache[(i,cur_amount)] = min(skip, dont_skip)
            return cache[(i,cur_amount)]
        res = top_down(0, 0)
        return res if res != float('inf') else -1