class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        
        mismatch=0     
        left=0
        right=len(s)-1
        

        def ispalindrome(s,left,right):
          
            if left>right or left==right:
                return True
            
            elif s[left]==s[right]:
                left+=1
                right-=1
                return ispalindrome(s,left,right)
            
       
            nonlocal mismatch
            if mismatch==0:
                
                if right-left==1: return True
                 
                print(left,right)
                s1=s[left:right]
                s2=s[left+1:right+1]    
                print(s1," ",s2)   
                
        
                mismatch=1
                return ispalindrome(s1,0,len(s1)-1) or ispalindrome(s2,0,len(s2)-1)
                
               
            
            return False
                
        
        
        
        
        return(ispalindrome(s,0,len(s)-1))
        