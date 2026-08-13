class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = [-1]*len(nums1)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                 if nums2[j] == nums1[i]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            temp[i] = nums2[k]
                            break
                    break

        return temp

        