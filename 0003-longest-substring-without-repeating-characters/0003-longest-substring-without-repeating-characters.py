class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        #expand as long as we dont get a duplicate if we get a duplicate shrink as long as we can not get rid of the duplicate then expand again and repeat
        
        if not s: return 0
        char_set = set()
        
        mx=1
        left = 0 
        right = 0
        
        
        for right in range(len(s)):
            
            
            if s[right] not in char_set:
                
               # print("expanding")
                char_set.add(s[right])
                

                
            else:
                while (left<right):
                    #print("shrinking")
                    
                    if s[left]==s[right]:
                        
                    # we dont remove left because it is same as right and we did not add right when we first encountered it
                    
                        left+=1
                        break
                        
                    elif s[left]!= s[right]:   
                        #keep removing
                        char_set.remove(s[left])
                        left+=1
                        
                        
            mx=max(mx,right-left+1)
                
        return mx
                        
                        
                        
                
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
            
            
          
                