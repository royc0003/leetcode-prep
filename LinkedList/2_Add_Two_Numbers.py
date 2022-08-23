# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 edge cases:
        (1) for the '?', replace with the value of '0'
            1 -> 0
            2 -> ?
            
        (2) if we have an additional carryBit, remmeber to create a new node for it
        e.g.
        Carry = 1
            1 -> 
        ________
        res : 1 -> 1
    
        '''
        tailNode = ListNode()
        cur, carryBit = tailNode, 0 
        
        while l1 or l2:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0
            curSum = val1 + val2 + carryBit
            # set carry bit
            carryBit = curSum // 10 
            # cur val 
            curVal = curSum % 10 
            # create a new node
            cur.next = ListNode(curVal)
            
            # shift the nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        # handle edge case 2: where we have additinal bit
        if carryBit > 0:
            cur.next = ListNode(carryBit)
        
        return tailNode.next
        
        
        