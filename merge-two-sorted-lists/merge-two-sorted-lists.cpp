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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        ListNode* l3=new ListNode();
        ListNode* head=l3;
        
        while(l1!=NULL and l2!=NULL){
            
            if(l2->val>l1->val){
                l3->next=l1;
                l1=l1->next;
            }
            
            else{
                l3->next=l2;
                l2=l2->next;
            } 
            
        l3=l3->next;
        }
        if(l1!=NULL)    l3->next=l1;
        
        else if(l2!=NULL) l3->next=l2;
        
        
       return head->next; 
    
    }
};