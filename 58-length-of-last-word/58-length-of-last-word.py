class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s=list(s)
        s.reverse()
        
        cnt=0
        flag=0
        for i in range(len(s)):
            
            
            if s[i]==" " and flag==1:
                return cnt
            
            elif s[i]!=" ":
                cnt+=1
                flag=1
            
            
                
        return cnt