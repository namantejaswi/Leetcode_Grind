class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        
        p = int(log2(n))+1
        self.dp = [ [-1]*p for i in range(n)]
        
        for j in range(p):
            for i in range(n):
                if j==0:    self.dp[i][0] = parent[i]
                    
                elif self.dp[i][j-1] !=-1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
                    
                
        

    def getKthAncestor(self, node: int, k: int) -> int:
        
        while k>0 and node!=-1:
            p = int(log2(k))
            node = self.dp[node][p]
            
            k = k-2**p
            
        return node
            
        
            
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)