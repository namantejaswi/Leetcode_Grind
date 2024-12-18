class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        if len(s1)+len(s2)!=len(s3): return False
        
        dp = {}
        
        
        #dfs(i,j) determines is it possible to interleave starting from index i of s1 and index j of s2, our problem statement is to solve for dfs(0,0), we update i and j based on which of them matches with the 
        
        def dfs(i,j):
            
            if i== len(s1) and j==len(s2):
                
                return True 
            
            if (i,j) in dp: return dp[(i,j)]
            
            
            #if first string has characters left and the current character matches the character at index of i+j intervleavings already done and the next interleaving can be done i,e dfs(i+1,j) is True then return true
            
            if i<len(s1) and s1[i]==s3[i+j] and dfs(i+1,j):
                
                dp[(i,j)] = True
                return True
            
            #we dont use elif because we want to explore both conditions if both of the next characters are matching!
            
            if j<len(s2) and s2[j]== s3[i+j] and dfs(i,j+1):
                dp[(i,j)] = True
                return True

            
            else:   
                dp[(i,j)] = False
                return False
            
        return dfs(0,0)
        