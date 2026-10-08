# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        arr = []
        current = head
        Decimal = 0
        while(current is not None):
            Decimal = Decimal*2+current.val
            current = current.next

        return Decimal
        


        

        