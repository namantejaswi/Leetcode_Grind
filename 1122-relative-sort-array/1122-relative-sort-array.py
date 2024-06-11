class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        rem = []
        res = []
        s =set(arr2)
 
    
        count = {}
        
        for i in arr1:
            if i in s:
                
                if i not in count:  count[i]=1
                    
                else:   count[i]+=1
                    
            elif i not in s:    rem.append(i)        
            
            
        for i in arr2:
            
           
            for j in range(count[i]):  res.append(i)
            
        rem.sort()
        res.extend(rem)
        
        return res
            
    