# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next # save curr's next node
            curr.next = prev # reverse
            prev = curr # set prev to reverse for new curr's next
            curr = temp # set new curr
        return prev
