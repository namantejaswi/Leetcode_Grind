class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        
        res=[]
        for i in range(1,n+1):
            res.append([1]*i)
       
        for i in range (0,n):
            
            for j in range(1,len(res[i])-1):
                res[i][j]= res[i-1][j-1]+res[i-1][j]
            
            
        #print(res)
        return res
            
            