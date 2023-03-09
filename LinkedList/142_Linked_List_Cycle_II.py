# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        (1) Find the meeting point of fast and slow runner
            - Now both will always meet in the same spot in the loop
        (2) Put slow at the start of the race again, and decrement the speed of Fast by 1. This will ensure they meet at the start of the circle since both are `n-m` steps away from starting point.
        '''
        if not head:
            return None

        cur = head
        slow, fast = cur, cur
        intersect = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = True
                break
        if not intersect:
            return None

        slow = cur
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast