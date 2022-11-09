class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        length of string + delimiter
        
        Encode -> ["Hello", "Word"]
        str = "5#Hello"
        
        """
        res = ""
        for item in strs:
            len_str = len(item)
            res += str(len_str) + "#" + item
            
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0 
        while i < len(s):
            len_str = 0
            # get the total length of the string
            while s[i].isdigit():
                len_str*= 10
                len_str += int(s[i])
                i += 1
            # skip the delmiter sign
            res.append(s[i+1: i+1+len_str])
            i += 1 + len_str
        return res
                
            
            
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))