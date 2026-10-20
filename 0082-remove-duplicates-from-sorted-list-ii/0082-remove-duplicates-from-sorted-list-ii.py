# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while(temp is not None):
            if(temp.next and temp.val==temp.next.val):
                dup = temp.val

                while(temp and temp.val==dup):
                    temp = temp.next

                prev.next = temp


            else:
                prev = temp
                temp = temp.next

        return dummy.next
        