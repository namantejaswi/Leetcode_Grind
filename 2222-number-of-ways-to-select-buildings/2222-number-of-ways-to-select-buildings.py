class Solution:
    def numberOfWays(self, s: str) -> int:
        
        count={"0":0,"1":0,"01":0,"10":0,"010":0,"101":0}
        
        for i in range(len(s)):
            if s[i]=="0":
                count["0"]+=1
                count["10"]+=count["1"]
                count["010"]+=count["01"]
                
            if s[i]=="1":
                count["1"]+=1
                count["01"]+=count["0"]
                count["101"]+=count["10"]
                
        return count["010"]+count["101"]