class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)==0:  return[]
        
        
        digit_map={1:"",2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        q=deque(digit_map[int(digits[0])])
        
        for i in range(1,len(digits)):
            
            l=len(q)
            
            while l>0:
                
                v=q.popleft()
                for j in digit_map[int(digits[i])]:
                    
                    q.append(v+j)
                    
                l-=1
 
        return list(q)