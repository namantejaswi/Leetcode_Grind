class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # This is needed for ListNode to be compatible with heapq comparisons
        return self.val < other.val

class Solution:
    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Insert the head of each list into the min-heap
        for idx, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, idx, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            # Pop the smallest node
            val, idx, node = heappop(min_heap)

            # Add it to the result list
            current.next = node
            current = current.next

            # If there is a next node in the list, push it to the heap
            if node.next:
                heappush(min_heap, (node.next.val, idx, node.next))


        return dummy.next