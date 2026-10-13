# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head

        while(curr is not None):
            arr.append(curr.val)

            curr = curr.next

        i = 0 
        j = len(arr)- 1

        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i+= 1
            j -=1

        curr = head
        k = 0
        while(curr is not None):
            curr.val = arr[k]
            curr = curr.next
            k += 1

        return head
