class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxnum = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>maxnum:
                maxnum = arr[i]

        for j in range(len(arr)):
            if(arr[j]==maxnum):
                ans = j

        return ans

                


        