class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0 
        tmp_path = path.split("/")
        for item in tmp_path:
            if item == "." or not item:
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        str_builder = "/"
        str_builder += "/".join(stack)
        return str_builder