"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        old_to_new={}
        
        #use a hashmap with key as pld node and value as the new node created recurrsively
        
        
        def dfs(node):
            
            if node==None:   return 
            
            else:
                
                clone=Node(node.val,[])   #create a node but will have no neighbor assigned
                
                old_to_new[node]=clone #add the new node corresponding to orignal in the map
                
                for i in node.neighbors:    #iterate the orignal node neighbor
                    
                    if i in old_to_new:     #if a neighbor of orinal node in map, i.e key 
                                            #append its corresponding new node neighbor
                                            # i.e the value of the key neighbor which is
                                            # the new node as the neighbor on clone
                        
                        clone.neighbors.append(old_to_new[i])
                        
                    else:
                        
                        clone.neighbors.append(dfs(i))   #if i is not in hashmap key
                                                        #recurssive call
                return clone
                
        return dfs(node)
        
        
        
        
        
        
        
    

        
        