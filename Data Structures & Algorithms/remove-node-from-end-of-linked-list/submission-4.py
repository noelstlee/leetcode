# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        scout = head
        length = 0

        while scout:
            scout = scout.next
            length += 1
        
        print(length)
        
        prev = None
        post = None
        delNode = head

        if length == 1:
            return None
        
        index = length - n

        if index == 0:
            head = head.next
            return head
            
        for _ in range(length - n):
            prev = delNode
            delNode = delNode.next
            if delNode:
                post = delNode.next
            else:
                post = None
        
        prev.next = post

        return head
