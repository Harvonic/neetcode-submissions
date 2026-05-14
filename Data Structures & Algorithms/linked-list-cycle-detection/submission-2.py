# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # seen = {}

        # current = head

        # while current:
        #     if current in seen:
        #         return True
        #     seen[current] = True
        #     current = current.next
        
        # return False

        # fast and slow approach
        slow = head
        if not slow:
            return False
            
        n = slow.next
        if not n:
            return False
        fast = n.next

        while fast and slow:
            if fast == slow:
                return True
            
            slow = slow.next
            n = fast.next
            if not n:
                return False
            fast = n.next
        
        return False
        