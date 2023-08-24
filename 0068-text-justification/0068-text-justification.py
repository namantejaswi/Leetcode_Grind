class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        res = []
        line = []
        count_letters = 0
        
        for w in words:
            
            #if line is complete
            if count_letters + len(line) + len(w) > maxWidth:
                size = max(1, len(line)-1)
                
                #this line is complete we apply spacing round robin manner so if we have a single word it will be left justified, this helps us avoid writting specific edge case of single word 
                
                for i in range(maxWidth-count_letters):
                    
                    index = i%size
                    line[index] += ' '
                    
                res.append(''.join(line))
                # reset lin and count_letters
                
                line, count_letters =[], 0
                
                
            # if line is not complete we can addd something
            
            line.append(w)
            count_letters += len(w)
        

        #last line all extra spaces at the end of last word and 1 b/w them as usual
        
        
        last_line =" ".join(line)
        #print(last_line)
        
        extra_spaces = maxWidth-len(last_line)
        
        for i in range(extra_spaces):
            last_line +=" "
        res.append(last_line)
        return res