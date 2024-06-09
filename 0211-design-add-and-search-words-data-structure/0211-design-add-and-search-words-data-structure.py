class Trie_Node:
    
    def __init__(self):
        self.children = dict()
        self.is_end = False


class WordDictionary:
    
    
    def __init__(self):
        self.root = Trie_Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie_Node()
                
            #move to next node i.e the chid node we insert 
            node = node.children[char]
            
        node.is_end = True
        
        

    def search(self, word: str) -> bool:
        return self.search_in_node(word,0,self.root)
        
    #we need to use dfs with index for . 
    
    def search_in_node(self,word,index,node:Trie_Node) -> bool:
         
        if index == len(word):
            return node.is_end
        
        char = word[index]

        if char == ".":
            
            for child in node.children.values():
                if self.search_in_node(word,index+1,child):
                    
                    return True
        elif char not in node.children: return False
        
        
        elif char in node.children:
            return self.search_in_node(word,index+1,node.children[char])
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)