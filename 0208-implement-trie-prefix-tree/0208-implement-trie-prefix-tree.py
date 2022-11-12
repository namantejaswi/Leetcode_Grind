class TreeNode:
    
    def __init__(self):
        self.children={}
        self.is_end=False



class Trie:

    def __init__(self):
        self.root=TreeNode()
        

    def insert(self, word: str) -> None:
        
        curr_node=self.root
        for ch in word:

            if ch not in curr_node.children:
                
                curr_node.children[ch]=TreeNode()
                curr_node=curr_node.children[ch]
            
            else:   curr_node=curr_node.children[ch]
                
        curr_node.is_end=True

    def search(self, word: str) -> bool:
        
        curr_node=self.root
        
        for ch in word:
            
            if ch in curr_node.children:
                curr_node=curr_node.children[ch]
                
            else:   return False
            
        return curr_node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        
        curr_node=self.root
        
        for ch in prefix:
            
            if ch in curr_node.children:
                curr_node=curr_node.children[ch]
                
            else:   return False
            
        return True
                
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)