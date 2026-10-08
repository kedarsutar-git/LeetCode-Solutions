# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        arr = []
        current = head

        while(current is not None):
            arr.append(current.val)
            current = current.next


        Decimal = 0
        for i in range(len(arr)):
            Decimal = Decimal*2+arr[i]

        return Decimal 

        


        

        