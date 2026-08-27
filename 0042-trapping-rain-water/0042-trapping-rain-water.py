class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0 ,len(height) - 1
        leftmax ,rightmax = 0 ,0 
        total = 0 

        while(left<right):
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])

            if(leftmax<rightmax):
                total += leftmax - height[left]

                left += 1

            else:
                total += rightmax - height[right]

                right -= 1

        return total
         



            
        
            

                  

             




        