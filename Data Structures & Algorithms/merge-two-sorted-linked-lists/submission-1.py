# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # current = list1
        # if list1 and list2:
        #     current = list1 if list1.val < list2.val else list2
        # elif list2:
        #     current = list2

        # other = list1 if current != list1 else list2

        # head = current


        # while current and other:
        #     val = other.val

        #     while current.next and current.next.val < val:
        #         current = current.next
            
        #     temp = other
        #     other = other.next

        #     temp.next, current.next = current.next, temp

        #     current = current.next

        # return head

        # standard approach using dummy
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return dummy.next




        