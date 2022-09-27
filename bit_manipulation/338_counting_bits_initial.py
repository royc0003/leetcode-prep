class Solution:
    def countBits(self, n: int) -> List[int]:
        i, res = 0, [0]*(n+1)
        def countBit(num):
            res = 0
            while num:
                res +=1 if num%2 == 1 else 0
                num = num // 2
            return res
            
        while i < len(res):
            res[i] = countBit(i)
            i += 1
        return res
        
        