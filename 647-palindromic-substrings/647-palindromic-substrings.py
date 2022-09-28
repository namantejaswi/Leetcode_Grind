class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #brute force
        #def ispal(s,l,r):   
            #while(r>l):
                
             #   if s[l]!=s[r]:  return False
                
              #  else:   
               #     l+=1
                #    r-=1
            #return True
                    
        #res=0    
        #for i in range(len(s)):
         #   for j in range(i,len(s)):
          #      res+=ispal(s,i,j)     
        #return res
        
        #we start at central point and build
        def expand(s,l,r):
            res=0
            while l>=0 and r <len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        
        cnt=0
        for i in range(len(s)):
            cnt+=expand(s,i,i)
            cnt+=expand(s,i,i+1)
            
        return cnt
                
                
                
        
        
        
        
            
        