# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        non-optimal solution
        
        Solution:
        1. use fast and slow pointer to split the linked-list into two halves
        2. reverse the right-hand side of the linked list
        3. peform inter-leaving where l1 points to l2 and l2 points to the next val of l1
        
        """
        cur = head
        slow, fast = cur, cur
        
        # Step 1: fast and slow pointers; to split into two halves
        # of the linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # step 3: Perfomr Interleaving
        l1, l2 = head, prev
        while l1 and l2:
            next_l1 = l1.next
            next_l2 = l2.next
            l1.next = l2
            l1 = next_l1
            l2.next = l1
            l2 = next_l2
        
    
            
            
            
            
            
            
        
            