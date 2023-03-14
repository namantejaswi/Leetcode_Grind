class Solution:
    def partitionString(self, s: str) -> int:
        
        
        
        curr_set = set()
        cnt=0
        
        for i in range(len(s)):
            
            
            print(s[i])
            
            if s[i] in curr_set:
                cnt+=1
                print(curr_set)
                curr_set=set(s[i])
                
            else:       
                curr_set.add(s[i])
            
            
        return cnt+1