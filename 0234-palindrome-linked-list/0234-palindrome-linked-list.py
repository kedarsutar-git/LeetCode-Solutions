# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        temp = head
        while(temp is not None):
            ans.append(temp.val)
            temp = temp.next

        i, j = 0, len(ans) - 1

        while(i<j):
            if ans[i] != ans[j]:
                return False

            i += 1
            j -= 1

        return True 

                    

        