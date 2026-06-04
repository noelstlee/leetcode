# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, newHead = None, head

        while newHead:
            temp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp

        return prev