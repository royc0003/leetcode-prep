class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        '''
        nlogn
        '''
        # nlogn
        costs.sort()
        _sum = 0 
        res = 0
        for r, cost in enumerate(costs):
            if (_sum + cost) > coins:
                break
            res += 1
            _sum += cost
        return res