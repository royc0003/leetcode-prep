# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        - delcare 2 pointers, and 
        - maintain the distance apart from each other.
        - and when the pointer ahead reaches null
        - the back pointer will be pointed to the desired node to be removed.
        
        Teaches you how 2 pointers can be used to remove node
        
        '''
        
        tailNode = ListNode()
        tailNode.next = head
        cur = tailNode
        
        nextPtr = head
        count = 0
        while count < n:
            nextPtr = nextPtr.next
            count += 1
        
        # move forward till the end
        while cur and nextPtr:
            cur = cur.next
            nextPtr = nextPtr.next
        
        cur.next = cur.next.next
        
        return tailNode.next
            
        
            
        
        