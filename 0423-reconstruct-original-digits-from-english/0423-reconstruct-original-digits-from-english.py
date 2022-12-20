class Solution:
    def originalDigits(self, s: str) -> str:
        
        freq= defaultdict(int,Counter(s))

        count={}
        
        count[0]=freq["z"]
        count[2]=freq["w"]
        count[4]=freq["u"]
        count[6]=freq["x"]
        count[8]=freq["g"]
        
        # h is only in three and eight
        count[3]=freq['h']-count[8]
        
        #f only in five and four
        count[5]=freq["f"]-count[4]
        
        #v
        count[7]=freq["v"]-count[5]
          
        #i
        count[9]=freq["i"]-count[5]-count[6]-count[8]
        
        #n
        count[1]=freq['n']-count[7]-2*count[9]
        
        
        res=""        
        count=dict(sorted(count.items(),key=lambda x:x[0]))
        for k,v in count.items():
        
            if v!=0:    res+=str(k)*v
                
        return res