class Solution:
    def findContentChildren(self, student: list[int], cookie: list[int]) -> int:

        Students = sorted(student)
        Cookies = sorted(cookie)

        left = 0
        right = 0

        while left < len(Students) and right < len(Cookies):

            if Cookies[right] >= Students[left]:
                right += 1
                left += 1
            else:
                right += 1

        return left