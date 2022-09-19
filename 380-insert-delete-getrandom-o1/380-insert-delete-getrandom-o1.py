class RandomizedSet:

    def __init__(self):
        
        
        self.dic=dict()
        self.idx_to_key=[]

    def insert(self, val: int) -> bool:
        
        if val in self.dic: return False
        
        else:   
            #we use index we store the element in the list as the value in dic
            #we initially have an empty list and then append it
            self.dic[val]=len(self.idx_to_key)
            self.idx_to_key.append(val)
            return True
            

    def remove(self, val: int) -> bool:
        
        #to remove the element the key val pair in map will give the index we need to 
        #pop from the array
        
        
        if val not in self.dic: return False
        
        else:
            
            idx_to_remove=self.dic[val]  
            
            last_number=self.idx_to_key[-1]
            
            self.idx_to_key[idx_to_remove]=last_number
            
            self.dic[last_number]=idx_to_remove                     
            
            del self.dic[val]
            self.idx_to_key.pop()
            
            return True
        
        
    def getRandom(self) -> int:
        
        import random
        #return random.choice(list(self.dic.keys()))
        return random.choice(self.idx_to_key)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()