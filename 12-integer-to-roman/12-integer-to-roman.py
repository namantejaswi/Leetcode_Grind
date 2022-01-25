class Solution:
    def intToRoman(self, num: int) -> str:
        
        #stupid as fuck question
        
        dic={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M", 900:"CM",
            400:"CD",90:"XC",40:"XL",9:"IX",4:"IV"}
        
        
        dic=dict(sorted(dic.items(),reverse=True))
        res=""
        
        #print(dic)
        for i in dic:
            res += (num//i) * dic[i]
            num %= i
        
        return res
    
    
    
    
    
    