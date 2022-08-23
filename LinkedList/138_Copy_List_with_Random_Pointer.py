"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        3 Steps Process.
        Step 1: Put the new node on the side of the old pointer, such that,
        # A and A' 
        Step 2: Fix the random pointer
        Step 3: Unweave
        '''
        
        if not head:
            return
        
        cur = head 
        # Step 1: Put the new node on the side of the old pointer, such that,
        # A and A' 
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next
            
            
        # Step 2: Fix the random pointer, point to random pointer.next
        curMain = head
        while curMain:
            curMain.next.random = curMain.random.next if curMain.random else None
            curMain = curMain.next.next
        
        # Step 3: Unweave
        oldPointer = head
        newPointer = oldPointer.next 
        res = oldPointer.next 
        while oldPointer:
            oldPointer.next = oldPointer.next.next
            newPointer.next = newPointer.next.next if newPointer.next else None 
            oldPointer = oldPointer.next
            newPointer = newPointer.next 
        
        return res
        
        
        
            
        