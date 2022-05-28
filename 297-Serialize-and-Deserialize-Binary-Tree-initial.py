# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Iterative method Pre-order method.
        Also notice that for iterative method Pre-order,
        its always append:
        (1) right
        (2) left 

        and post-order would be:
        (1) left
        (2) right
        """
        
        serialize_str = []
        
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            str_builder = ""
            if cur_node is None:
                str_builder = "null"
            else:
                str_builder += str(cur_node.val)
                
            serialize_str.append(str_builder)
            
            if cur_node:
                stack.append(cur_node.right)
                stack.append(cur_node.left)        
        
        # remeber to serialize using string concat
        return ",".join(serialize_str)
        
        

    def deserialize(self, data):
        """
        Notice that there's unecessary use of passing of `data` into dfs()

        """
        global_counter = [0]
        
        data = data.split(",")
        
        def dfs(data):
            if data[global_counter[0]] == "null" or global_counter[0] > len(data)-1:
                global_counter[0] += 1
                return None
            
            cur_node = TreeNode(data[global_counter[0]])
            # increment total counter
            global_counter[0] += 1
            
            cur_node.left = dfs(data)
            cur_node.right = dfs(data)
            
            
            return cur_node
        
        res = dfs(data)
        
        return res
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))