class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        if len(skill)%2!=0: return -1
        
        
        skill.sort()
        
        s = skill[0] + skill[-1]
        chem = 0
        
        for i in range(len(skill)//2):
            
            if skill[i]+skill[len(skill)-1-i] == s: 
                chem += skill[i]*skill[len(skill)-1-i]
                
            else: return -1
        
        return chem
            
        