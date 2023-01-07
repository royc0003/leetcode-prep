class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def bruteforce(i, cur_amount):
            if cur_amount == amount:
                return 0 
            if i >= len(coins):
                # max
                return float('inf')
            # skip
            skip = bruteforce(i+1, cur_amount)
            # dont skip
            potential_amount = cur_amount + coins[i]
            dont_skip = float('inf')
            if potential_amount <= amount:
                res = bruteforce(i, potential_amount)
                if res != float('inf'):
                    dont_skip = 1 + res
            return min(skip, dont_skip)
        res = bruteforce(0, 0)
        return res if res != float('inf') else -1

        