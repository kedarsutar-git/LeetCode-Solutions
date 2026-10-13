# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        arr = []
        curr = head

        while(curr is not None):
            arr.append(curr.val)
            curr = curr.next

        array = sorted(arr)

        k = 0 
        curr = head

        while(curr is not None):
            curr.val = array[k]
            curr = curr.next
            k += 1

        return head


                