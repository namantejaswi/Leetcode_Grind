class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        
        #we need to split the domain using .  
        
    
        d = Counter()
        
        for domain in cpdomains:
            
            count, domain = domain.split()
            
            count = int(count)
            
            sub_domain = domain.split('.')
            
            for i in range(len(sub_domain)):
                
                d[".".join(sub_domain[i:])]+=count
                
                
       # print(d)
        
        return ["{} {}".format(cnt,dom) for dom,cnt in d.items()]
        