class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0 
        index = 0
        for r, char in enumerate(chars):
            if ((r+1) < len(chars) and chars[r+1] != char) or r == len(chars)-1:
                if (r-l+1) == 1:
                    l = (r+1)
                    chars[index] = char
                    index += 1
                    continue
                cur_len_str = str(r-l+1)
                chars[index] = char
                index += 1
                for c in cur_len_str:
                    chars[index] = c
                    index += 1
                l = (r+1)
        return index