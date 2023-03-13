class Solution:
    def decodeString(self, s: str) -> str:
        '''
        recursive solution
        - time complexity: O(N)
        - Space complexity: O(max(Nesting))

        iterate string from i <-- 0:
        - if cur_val is an alphabet, put into stringbuilder
        - if cur_val is number then:
            update total multiplier
        - if cur_val == '[':
             - perform multiplier * recursion(i+1)
             - update existing string strBuilder
             - update current index with overall_index
             - reset multiplier counter
        - if cur_val == ']':
            - update overall_index = (i+1) 
            - break
        '''
        next_index = [0]
        def dfs(i, str_builder):
            multiplier = 0
            str_builder = ""
            while i < len(s):
                if s[i].isalpha():
                    str_builder += s[i]
                    i += 1 
                    continue
                elif s[i].isdigit():
                    multiplier *= 10
                    multiplier += (ord(s[i]) - ord('0'))
                    i += 1
                    continue
                elif s[i] == '[':
                    if multiplier == 0:
                        multiplier = 1
                    res = multiplier * dfs(i+1, str_builder)
                    # reset multiplier
                    multiplier = 0
                    str_builder += res
                    i = next_index[0]
                else:
                    next_index[0] = i + 1
                    break
            return str_builder
        return dfs(0, "")