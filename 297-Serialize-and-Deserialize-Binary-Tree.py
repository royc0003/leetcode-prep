# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        serialize_str = []
        
        def dfs(root):
            if root is None:
                serialize_str.append("null")
                return 
            
            serialize_str.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        # serialize using concant
        return ",".join(serialize_str)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        global_counter = [0]
        
        data = data.split(",")
        
        def dfs():
            if data[global_counter[0]] == "null":
                # increment total counter
                global_counter[0] += 1
                return None
            
            cur_node = TreeNode(data[global_counter[0]])
            # increment total counter
            global_counter[0] += 1
            
            cur_node.left = dfs()
            cur_node.right = dfs()
            
            return cur_node
        
        res = dfs()
        
        return res