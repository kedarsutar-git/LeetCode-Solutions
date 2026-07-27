class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        secondlargest = 0

        for num in nums:
            if(num>=largest):
                secondlargest = largest
                largest = num
            
            elif(num>secondlargest):
                secondlargest = num
        
        return (largest-1) * (secondlargest-1)

                

        