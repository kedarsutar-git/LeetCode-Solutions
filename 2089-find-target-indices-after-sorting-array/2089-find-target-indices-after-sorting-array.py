class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        def first(nums):
            start = 0
            end = len(nums)-1
            ans = -1

            while(start<=end):
                mid = start + (end-start)//2

                if(nums[mid]==target):
                    ans = mid
                    end = mid -1

                elif(nums[mid]>target):
                    end = mid - 1

                else:
                    start = mid +1

            return ans 


        def last(nums):
            ans = -1
            start = 0
            end = len(nums)-1

            while(start<=end):
                mid = start + (end - start)//2
                if(nums[mid]==target):
                    ans = mid

                    start = mid +1

                elif(nums[mid]<target):
                    start = mid +1

                else:
                    end = mid -1

            return ans 


        First = first(nums) 
        if(First==-1):
            return []

        Last = last(nums)
        return list(range(First,Last+1))

