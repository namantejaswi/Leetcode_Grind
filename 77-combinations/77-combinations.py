class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        result=[]
        
        
        def helper(start,cc):
            
            #Base case
            if len(cc)==k:
                result.append(cc[:])   #or use result.append(cc.copy()) 
                #print(cc)
                return

            for i in range(start,n+1):  
                # we choose start as  we want the combinations not the permutations                 #so we only take elements in front of curr to avoid permutation
                
                cc.append(i)    #we add the firt number to current combination
                
                helper(i+1,cc)  #call from next no. with current cc
                
                cc.pop()

                    
        helper(1,[])
            
        
        return result