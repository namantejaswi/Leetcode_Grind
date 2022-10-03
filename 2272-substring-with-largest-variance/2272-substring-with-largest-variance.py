class Solution:
    def largestVariance(self, s: str) -> int:
        
        
        
        chars=list(set(s))
        res=0
        
        
        for i in range(len(chars)):
            
            for j in range(i+1,len(chars)):
                
                ch1,ch2=chars[i],chars[j]
                
                diff=0
                
                max_diff=0
                min_diff=0
                
                last_c1_diff=0
                last_c2_diff=0
                
                c1_occured=False
                c2_occured=False
                
                
                
                for ch in s:
                    if ch==ch1:
                        c1_occured=True
                        diff+=1
                        max_diff=max(max_diff,last_c1_diff)
                        
                        last_c1_diff=diff
                        
                    elif ch==ch2:
                        
                        c2_occured=True
                        diff-=1
                        min_diff=min(min_diff,last_c2_diff)
                        last_c2_diff=diff
                        
                    else:
                        continue
                        
                        
                    if c1_occured and c2_occured:
                        res=max(res,diff-min_diff,max_diff-diff)
                        
        return res
                        
                        
                        
                        
                        
                    