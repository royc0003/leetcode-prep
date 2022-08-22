# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
       1. Iterate through and get the numerical value
       2. Use `%` to get the reverse of both digits
       3. add the results. 
            1
       2 4 3 
       5 6 4 
       -------
       7 0 
       
       calculating_bit = sum // 10 
       [9,9,9,9,9,9,9]
       [9,9,9,9      ]
       ------------------
        8 9 9 9 
        
        perhaps we can do padding? 
        
        12 % 10 == 2 (value)
        12 // 10 = 1 (carry over bit)
       
       
       
        '''
        headL1, headL2 = l1, l2
        carryOverBit = 0
        tailNode = ListNode()
        cur = tailNode
        
        while l1 and l2:
            curSum = carryOverBit + l1.val + l2.val
            # Set carry over bit 
            carryOverBit = curSum // 10 
            # reset current l1 val
            l1.val = curSum % 10 
            # set the current node
            cur.next = l1 
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        # handle edge case 
        # check if l1 or l2 is still the longest string
        while l1: 
            curSum = carryOverBit + l1.val
            carryOverBit = curSum // 10 
            l1.val = curSum % 10 
            cur.next = l1 
            cur = cur.next
            l1 = l1.next

        while l2:
            curSum = carryOverBit + l2.val
            carryOverBit = curSum // 10 
            l2.val = curSum % 10 
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        
        if carryOverBit > 0:
            cur.next = ListNode(carryOverBit)
            
        return tailNode.next
            
        
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        