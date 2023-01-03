class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        
        l=len(strs[0])
        
        cnt=0
        for i in range(0,l,1):
            
            for j in range(1,len(strs),1):
                
                if strs[j][i]<strs[j-1][i]:
                    cnt+=1
                    break
                    
        return cnt