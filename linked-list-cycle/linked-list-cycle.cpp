/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        
         if(head==NULL)              //Empty linked list
            return false;
        
        ListNode * slow_ptr=head;
        ListNode * fast_ptr=head->next;      
       
        //that is we are not at the end
        while(slow_ptr!=NULL and fast_ptr!=NULL and fast_ptr->next!=NULL){
                
            if(slow_ptr==fast_ptr){          
                /*cout<<"Cycle Detected"<<slow_ptr<<fast_ptr; 
                cout<<"Pointers have same address as they are pointing to same node and thus they have meet";*/
                return true;
                }
            slow_ptr=slow_ptr->next;        //Increase one node at a time
            fast_ptr=fast_ptr->next->next;  //Jump two nodes at a time
    
        
            }
        return false; // The cars on race track(pointers) don't meet => no cycle
                 
        }
        
};