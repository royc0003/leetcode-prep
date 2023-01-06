class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        def memoization(i, total_zeroes, total_ones):
            '''
            O(N*M)
            '''
            if i == len(strs):
                return 0
            if (i, total_zeroes, total_ones) in cache:
                return cache[(i, total_zeroes, total_ones)]
            # count number of potential zeroes and ones
            potential_zeroes, potential_ones = 0, 0 
            cur_num = strs[i]
            for digit in cur_num:
                if digit == '1':
                    potential_ones += 1
                else:
                    potential_zeroes += 1
            # choose to skip
            skip = memoization(i+1, total_zeroes, total_ones)
            # choose not to skip
            do_not_skip = -1
            if total_zeroes+potential_zeroes <= m and total_ones+potential_ones <= n:
                do_not_skip = 1 + memoization(i+1, total_zeroes+potential_zeroes, total_ones+potential_ones)
            cache[(i, total_zeroes, total_ones)] = max(skip, do_not_skip)
            return cache[(i, total_zeroes, total_ones)]
        
        return memoization(0, 0, 0)


