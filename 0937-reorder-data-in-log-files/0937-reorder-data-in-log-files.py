class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        
        letters=[]
        digits=[]
        
        
        for log in logs:
            
            
            if log.split()[1].isdigit():  
                digits.append(log)
                
            else:   letters.append(log)
    

        #sort the by alphabetical order when same sort by starting identifier
        letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))    
        
        
        res=letters
        res.extend(digits)
        
        return res