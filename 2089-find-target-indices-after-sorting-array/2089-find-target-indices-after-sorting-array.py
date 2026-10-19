class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def first(nums):
            ans = -1
            start, end = 0, len(nums) -1

            while(start<=end):
                mid = start + (end - start)//2

                if(nums[mid]==target):
                    ans = mid
                    end = mid - 1

                elif(nums[mid]>target):
                    end = mid - 1

                else:
                    start = mid + 1

            return ans 


        def last(nums):
            ans = -1
            start, end = 0, len(nums) - 1

            while(start<=end):
                mid = start + (end - start)//2
                if(nums[mid]==target):
                    ans = mid
                    start = mid + 1

                elif(nums[mid]<target):
                    start = mid + 1

                else:
                    end = mid - 1

            return ans 
        First = first(nums)
        Last = last(nums)
        if(First==-1):
            return []

        return list(range(First,Last+1))


                    



'''

Brute force method

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if(nums[i]==target):
                ans.append(i)

        return ans

        '''