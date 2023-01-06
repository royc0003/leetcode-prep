class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def bruteforce(i, total_zeros, total_ones):
            '''
            O(2^n)
            '''
            if i == len(strs):
                return 0
            cur_num = strs[i]
            potential_zeroes, potential_ones = 0, 0 
            for digit in cur_num:
                if digit == '1':
                    potential_ones += 1
                else:
                    potential_zeroes += 1
            # choose to skip
            skip = bruteforce(i+1, total_zeros, total_ones)
            # choose not to skip
            do_not_skip = -1
            if total_zeros+potential_zeroes <= m and total_ones+potential_ones <= n:
                do_not_skip = 1 + bruteforce(i+1, total_zeros+potential_zeroes, total_ones+potential_ones)

            return max(skip, do_not_skip)
        
        return bruteforce(0, 0, 0)