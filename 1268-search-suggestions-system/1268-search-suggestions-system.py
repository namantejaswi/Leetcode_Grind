class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        l=0
        r=len(products)-1
        res = []
        products.sort()
        
        for i, w in enumerate(searchWord):
            while l<=r and (len(products[l])<=i or products[l][i]!=w):
                l+=1
                  
            while l<=r and (len(products[r])<=i or products[r][i]!=w):
                r-=1    
        
            res.append(products[l:min(r+1,l+3)])
        
        return res

        
        