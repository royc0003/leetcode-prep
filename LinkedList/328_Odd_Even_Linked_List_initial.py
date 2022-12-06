# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 -> 1      |  -> 3 -> 5
        
        '''
        if not head:
            return head
        a, b = head, head.next
        tail = b
        while a != None and b != None:
            a_prime = a.next.next if a.next else None
            b_prime = b.next.next if b.next else None
            a.next = a_prime
            b.next = b_prime
            if a.next:
                a = a.next
            b = b.next
        a.next = tail
        return head




