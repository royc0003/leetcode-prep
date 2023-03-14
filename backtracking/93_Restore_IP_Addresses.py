class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def dfs(i, dot_count):
            if i == len(s) or (dot_count == 0 and int(s[i:]) > 255) or (dot_count == 0 and len(s[i:]) >= 2 and ord(s[i]) == ord('0')):
                return
            if dot_count == 0 and int(s[i:]) <= 255:
                copy_path = path[:] # deep-copy
                copy_path.append(s[i:])
                copy_path = ".".join(copy_path)
                res.append(copy_path)
                return
            cur_s = ""
            for j in range(i, len(s)):
                # eliminates all non-int
                if ord(s[j]) < ord('0') or ord(s[j]) > ord('9'):
                    continue
                if len(cur_s) < 3:
                    cur_s += s[j]
                    if int(cur_s) < 0 or int(cur_s) > 255:
                        break
                    if len(cur_s) >= 2 and cur_s[0] == '0':
                        break
                    # select path
                    path.append(cur_s)
                    dfs(j+1, dot_count - 1)
                    path.pop()
        dfs(0, 3)
        return res