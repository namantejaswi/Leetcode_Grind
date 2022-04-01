/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
    
    /* Iterative Approach 
        we need to flip the link direction but before we do that we
        need to store the previous element to which we will join the
        present link and the orignal next element through which we
        will traverse ahead in the list
    */
    
        ListNode* prev_node=NULL;
        ListNode* next_node=NULL;
        
        while(head!=NULL){
            
            next_node=head->next;  //To store Orignal next node to move through ll
            head->next=prev_node;  //Flip the link to the previous node  
            
            prev_node=head;        //Iterate through the list updating previous as
            head=next_node;        //current and head to orignal next so we move 
        }                          //through the list.
        return prev_node;
        
    }
};