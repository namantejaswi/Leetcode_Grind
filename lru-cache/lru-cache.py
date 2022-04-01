#For O(1) get and 0(1) put we need to use a hashmap with key as the first number #of the pair and the value as the entire node pair. The keys are also maintained #as a doubly linked list with a dummy head and a dummy tail, which we use to move
#the last updated item to the top so the least recently used item stays on the
#bottom(qeue)

class DLL_Node():
    def __init__(self):
        self.key=0
        self.value=0
        self.prev=None
        self.next=None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLL_Node()
        self.tail = DLL_Node()
        
        #Initially the dll is empty we only have head and tail
        #h-->T
        #h<--T
        self.head.next=self.tail
        self.tail.prev=self.head
     
        #Hashmap of key as first int and value as the complete node pair address
        
        self.map={}
        
        self.size=0
    
    def add_node(self,node):
        
        #We want the new node on top   
                                            #h==h.next (or tail for 1st add)
        
        node.prev = self.head               #h<--n
        node.next = self.head.next          #h<--n-->h.next(orignal 1st element)
        
        self.head.next.prev = node          #h<--n==h.next(orignal)  
        self.head.next = node
    
    
    def remove_node(self,node):
        
        prev=node.prev
        new_next=node.next
        
        prev.next=new_next
        new_next.prev=prev
        
        
    def move_to_head(self,node):
        
        #This function is called whenever we add or get so as to make the element
        #most recently used(get) elemen to the top
        
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self):
        
        #Return the last element pointing to tail
        
        res=self.tail.prev
        self.remove_node(res)
        return res
    
    def get(self, key: int) -> int:
        
        node_val=self.map.get(key,None)
        if not node_val:                        
            return -1
         
        self.move_to_head(node_val)
        return node_val.value

    def put(self, key: int, value: int) -> None:
        
        #check if value in val pair node map
        node_val=self.map.get(key)
        
        if not node_val:
            new_node = DLL_Node()
            new_node.key = key
            new_node.value=value
            
            self.map[key]=new_node
            self.add_node(new_node)
            self.size+=1
            
            if self.size>self.capacity:
                #Remove the least recently used that is elment at tail
                
                tail=self.remove_tail()
                del self.map[tail.key]
                self.size-=1
            
        else:
            node_val.value=value
            self.move_to_head(node_val)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


