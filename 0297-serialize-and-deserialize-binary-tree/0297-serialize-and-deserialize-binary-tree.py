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
        
        if not root: return ""
        
        q = deque()
        q.append(root)
        res = ""
        
        while q:
            node = q.popleft()
            if not node:
                res += 'None,'
            
            else:
                
                res += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
                
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q= deque()
        q.append(root)
        i=1
        
        while q and i<len(data):

            node = q.popleft()
            
            
            if data[i]!="None":
                left=TreeNode(int(data[i]))
                node.left=left
                q.append(left)
                
            i+=1
            
            if data[i]!="None":
                
                right=TreeNode(int(data[i]))
                node.right=right
                q.append(right)

            i+=1
            
        return root
                
                
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))