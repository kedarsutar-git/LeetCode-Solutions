class Solution:
    def subsets(self,nums:List[int]) -> List[List[int]]:
        arr = []
        def subseq(nums,index,current):
            
            if(index==len(nums)):
                arr.append(current)
                return

            subseq(nums,index+1,current+[nums[index]])    
            subseq(nums,index+1,current)

        subseq(nums,0,[])

        return arr




        