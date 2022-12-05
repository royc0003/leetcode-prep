# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        tortoise and hare algorithm
        floyd's algo
        1  -> 2 -> 3 -> 4 -> 5 -> 6
                   x.        x                                             
        
        '''
        cur = head
        slow, fast = cur, cur
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        if fast.next:
            slow = slow.next
        
        return slow
        
            
        