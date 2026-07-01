class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        start = 1
        end = position[len(position)-1] - position[0]
        ans = -1

        while(start<=end):
            mid = start + (end - start)//2

            if(self.isValid(mid,m,position)):
                ans = mid

                start  = mid + 1

            else:
                end = mid - 1

        return ans 


    def isValid(self,mid,m,position):
        pos = 0
        count = 1
        for i in range(1,len(position)):
            if(position[i]-position[pos]>=mid):
                count +=1
                pos = i

                if(count==m):
                    return True 

        return False


