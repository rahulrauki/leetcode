# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:# the idea is while parsing through the list with double the speed, the slow will be at the centre element of fast at any given time
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while head.next:
            if not fast or not fast.next: return slow
            slow = slow.next
            fast = fast.next.next
        else: return head
        