# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        current = head
        arr = []

        while(current is not None):
            arr.append(current.val)

            current = current.next

        i = left - 1
        j = right - 1

        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+= 1
            j -= 1


        curr = head
        k = 0
        while(curr is not None):
            curr.val = arr[k]
            curr = curr.next
            k += 1

        return head
        




                    