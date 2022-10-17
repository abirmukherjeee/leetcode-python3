# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer, slow_pointer, meet_pointer = head, head, None

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                meet_pointer = slow_pointer
                break

        if meet_pointer:
            start_pointer = head

            while start_pointer != meet_pointer:
                start_pointer = start_pointer.next
                meet_pointer = meet_pointer.next

        return meet_pointer
