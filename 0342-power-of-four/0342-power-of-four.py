class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        start = 0
        end = int(n**0.5)

        while(start<=end):
            mid = start+(end-start)//2

            if(n==4**mid):
                return True

            elif(n>4**mid):
                start = mid+1

            else:
                end = mid-1

        return False



        