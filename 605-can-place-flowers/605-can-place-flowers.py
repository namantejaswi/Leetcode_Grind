class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count=0
        
        for i in range(len(flowerbed)):
            
            if flowerbed[i]==0: 
                
                
                left = i==0 or flowerbed[i-1]==0
                #we can place when either we are at first index or previous is zero
                right = i==len(flowerbed)-1 or flowerbed[i+1]==0
                #we can place if either we are at last elment or next element is zero
                if left and right:
                    count+=1
                    flowerbed[i]=1
                
        return count>=n