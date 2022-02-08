class Solution:
    def addDigits(self, nums: int) -> int:
        
       
        s=0
    

        while(nums>0):
        
            s+=nums%10
            nums=nums//10
            
            
            if nums==0 and s>9:
                nums=s
                s=0
                
                
        return s
                