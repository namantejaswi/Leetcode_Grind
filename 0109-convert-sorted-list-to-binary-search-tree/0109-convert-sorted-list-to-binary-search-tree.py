# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        
        if not head:    return None
        mid = self.find_mid(head)
    #need to convert linked list node to tree node so that it has left and right ptr
        
        tree_node = TreeNode(mid.val)
        if head == mid: return tree_node    #only one elment
            
        tree_node.left = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(mid.next)
            
        return tree_node
            
        
    def find_mid(self,node):

        
        
        #we need to disconnect the remaining part of the linked list on the left side of the linked list since we are interval halving
        #we use previous to keep track of the elment just before mid
        
        prev=None
        
        if not node.next:   return node
        
        slow_ptr,fast_ptr=node,node

        while fast_ptr and fast_ptr.next:
            
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        #befor returning the mid set the next of prev to none instead of mid that
        #way we disconnect the linked list
        
        prev.next= None    
        return slow_ptr