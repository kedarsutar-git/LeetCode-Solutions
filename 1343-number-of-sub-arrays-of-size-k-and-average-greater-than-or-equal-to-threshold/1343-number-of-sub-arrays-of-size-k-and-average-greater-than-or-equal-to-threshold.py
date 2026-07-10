class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        current_sum = sum(arr[0:k])

        if(current_sum//k>=threshold):
            count +=1

        for i in range(k,len(arr)):
            
            current_sum = current_sum + arr[i] - arr[i-k]
           
            if(current_sum//k>=threshold):
                count += 1  

        return count           




        