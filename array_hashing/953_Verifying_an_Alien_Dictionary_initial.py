import collections
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # <key, val> <current_order_char, set(remaining_order)>
        # e.g. 'hla'
        # h: (l,a)
        # l: (a)
        # a: ()
        order_mapping = {}

        # create mapping
        for i in range(1, len(order)):
            prev_char= order[i-1]
            forward_set = [i for i in order[i::]]
            order_mapping[prev_char] = set(forward_set)  

        # edge case: last char in the order will point to null
        order_mapping[order[len(order)-1]] = set() # empty set  
        
        # checks if is in order
        def check_valid(cur_char, target):
            if target in order_mapping[cur_char]:
                return True
            return False
        
        for i in range(1, len(words)):
            prev_word, cur_word = words[i-1], words[i]
            
            a, b = len(prev_word), len(cur_word)
            shorter_len = a if a < b else b 
            # check for similar words, e.g. "app" in both ["apple", "app"]
            # and returns False if len of "app" is < len "apple"
            if prev_word[0:shorter_len] == cur_word[0:shorter_len] and b < a:
                    return False
            else:
                # checks for individual words
                for i in range(0, shorter_len):
                    prev_char, cur_char = prev_word[i], cur_word[i]
                    if prev_char != cur_char:
                        if not check_valid(prev_char, cur_char):
                            return False
                        else:
                            break
        return True
