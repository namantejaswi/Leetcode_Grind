class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        #Recurrence 
        
        #l1,l2
        
        l1=len(text1)-1
        l2=len(text2)-1
        
        memo=[[-1 for x in range(l2+1)] for y in range(l1+1)]

        def lcs(text1,text2,l1,l2):
            
            
            if(l1==-1 or l2==-1):
                
                return 0
            
            elif((memo[l1][l2])!=-1):
                return memo[l1][l2]    
            
            if(text1[l1]==text2[l2]):
                #print("match found",text1[l1],text2[l2])
                
                memo[l1][l2]=1+lcs(text1,text2,l1-1,l2-1)
                
                return memo[l1][l2]
                
            else:
                memo[l1][l2]= (max((lcs(text1,text2,l1-1,l2)),lcs(text1,text2,l1,l2-1)))
                return memo[l1][l2]
            
        return lcs(text1,text2,l1,l2)