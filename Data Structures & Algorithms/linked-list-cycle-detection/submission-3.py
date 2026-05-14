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
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        