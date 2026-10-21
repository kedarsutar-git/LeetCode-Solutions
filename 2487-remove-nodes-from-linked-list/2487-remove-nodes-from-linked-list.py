# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def removeNodes(self, head):
        # Step 1: Reverse the list
        head = self.reverse(head)

        max_so_far = head.val
        curr = head

        # Step 2: Remove smaller nodes
        while curr and curr.next:
            if curr.next.val < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.val

        # Step 3: Reverse again
        return self.reverse(head)
        return head