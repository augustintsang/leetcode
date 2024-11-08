# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        count = 0
        while ptr.next:
            ptr = ptr.next
            count = count + 1
        medium = math.ceil(count / 2)
        ptr2 = head
        while medium:
            ptr2 = ptr2.next
            medium = medium - 1
        return ptr2
            