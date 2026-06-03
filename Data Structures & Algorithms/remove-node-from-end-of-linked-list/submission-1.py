# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        lengthCheck = head
        while lengthCheck:
            lengthCheck = lengthCheck.next
            length += 1
        
        print(length)

        deleteNode = head
        prev = head

        print(length - n)

        for _ in range(length - n):
            prev = deleteNode
            deleteNode = deleteNode.next
        prev.next = deleteNode.next

        if length - n == 0:
            head = head.next

        return head