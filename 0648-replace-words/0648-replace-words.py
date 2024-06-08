class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        #We implement the trie of the dictionary and find the shortest common prefix
        
            
        words = sentence.split(" ")
        print(words)
        
        class Tree_Node:
            
            def __init__(self,char):
                
                self.value = char
                self.is_end = False
                self.children = dict()
                
        class Trie:
            
            def __init__(self):
                
                self.root = Tree_Node("")
                
            def insert(self,word):
                node = self.root
                for char in word:
                
                    if char not in node.children:
                        
                        node.children[char] = Tree_Node(char)
                        
                    node = node.children[char]
                    
                node.is_end = True
                
                
            def smallest_prefix (self, word):
                
                node = self.root
                prefix = ""
                
                for char in word:
                    
                    if char not in node.children:
                        return word
                    
                    prefix+=char
                    node = node.children[char]
                    
                    if node.is_end:
                        return prefix
                    
                return word
            
            
        Dictionary = Trie()
        for w in dictionary:
            Dictionary.insert(w)
            
        res = ""
        
        for w in words:
            res+=Dictionary.smallest_prefix(w)
            res+=" "
            
            
        return res[:-1]
        #print(Dictionary.smallest_prefix('cattle'))
        
                    
        
                        
                    
        