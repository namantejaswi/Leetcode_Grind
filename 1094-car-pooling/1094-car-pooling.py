class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """        
        
        status=[]
        
        for i in trips:

            status.append([i[0],i[1]])
            status.append([-i[0],i[2]])
            #-ve to subtract people at such timestamp
            
        #print(status)
        
        #sort by incident/event time 
        
        status.sort(key=lambda x:(x[1],x[0]))
        #Careful! for equal instance time which may be start or end 
        #use least number of passngers to break the tie
        
        #print(status)
        
        
        n_people=0
        
        #print(status)
        for i in status:
            
            n_people+=i[0]
            
            if n_people>capacity:
                
                return False
            
        return True
            
            
        
        
        
        