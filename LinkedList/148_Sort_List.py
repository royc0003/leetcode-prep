# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        recursion method
        '''

        def get_mid(cur_node):
            slow, fast = cur_node, cur_node
            prev = slow # Attention, needed to break the list
                        # prev is one step slower than slow
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None # seal the end of the head
            return slow
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            mid = get_mid(head)
            left = merge_sort(head)
            right = merge_sort(mid)
            return merge(left, right)

        def merge(l1, l2):
            head = ListNode(0)
            dummy = head
            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            return head.next

        return merge_sort(head)