# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # initialize
        res = lists[0] # result linkedlist head

        for i in range(1, len(lists)):
            income = lists[i] # incomming linked list
            while income:
                compare = res # set compare to be resulting linked list head to compare from smallest
                prev = None

                while compare and compare.val <= income.val:
                    prev = compare
                    compare = compare.next # move onto next comparison

                next_income = income.next

                # If we need to insert at the new head
                if prev == None:
                    income.next = res
                    res = income
                # Inserting in the middle or end
                else:
                    prev.next = income
                    income.next = compare
                
                income = next_income
        return res
                

    