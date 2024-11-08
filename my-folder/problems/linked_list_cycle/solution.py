# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]):
        ptr_slow = head
        ptr_fast = head
        while ptr_fast and ptr_fast.next:
            
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next
            if ptr_slow == ptr_fast:
                return True
        return False