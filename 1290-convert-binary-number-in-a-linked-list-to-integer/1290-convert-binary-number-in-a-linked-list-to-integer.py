#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        Decimal = 0
        current = head

        while(current is not None):
            Decimal = Decimal*2+current.val
            current = current.next


        return Decimal




'''
# Brute force method using Extra space O(n)

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

'''

        


        

        