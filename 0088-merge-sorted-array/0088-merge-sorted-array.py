class Solution:
    def merge(self,nums1,n,nums2,m):
        i = n-1  # last position of left array
        j = 0    # first position of right array
        while(i>= 0  and  j < m):
            if(nums1[i] > nums2[j]):
                nums1[i],nums2[j] = nums2[j],nums1[i]
                i-=1
                j+=1

            else:
                break 
        nums1[:n] = sorted(nums1[:n])
        nums2[:m] =  sorted(nums2[:m])

        nums1[n:] = nums2[:m]

        return nums1+nums2     

        
       
        