class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        i,j = 0,0

        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                temp.append(nums1[i])
                i+=1

            else:
                temp.append(nums2[j])
                j+=1


        while(i<len(nums1)):
            temp.append(nums1[i])
            i+=1

        while(j<len(nums2)):
            temp.append(nums2[j])
            j+=1

        n = len(temp)

        if(n%2==1):
             return temp[n//2]
        
        return (temp[n//2-1]+temp[n//2])/2


        
        