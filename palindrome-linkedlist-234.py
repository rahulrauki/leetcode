# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis = []
        while (head.next != None):
            lis.append(str(head.val))
            head = head.next
        lis.append(str(head.val))
        string = "".join(lis)
        if string == string[::-1]: return True
        return False