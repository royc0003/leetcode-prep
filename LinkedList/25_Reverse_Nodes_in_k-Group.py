# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Time-complexity: O(N)
        '''
        def reverse_node(node, last_node):
            prev = None
            cur = node
            while cur != last_node:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return prev

        if not head:
            return None #basecase
        
        a, b = head, head
        # we save the a to point to next direciton
        for _ in range(0, k):
            # base-case 2
            if not b:
                return head
            b = b.next
        new_head = reverse_node(a,b)
        a.next = self.reverseKGroup(b, k)
        return new_head
