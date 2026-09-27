class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        
        if(sum(source)!=sum(target)):
            return False

        return True 
'''
class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        for i in range(len(source)):
            for j in range(len(source)):
                if(i!=j):
                    source[j] = delta
                    source[i] = source[i] + source[j] - delta
                    source[j] = delta

        if(source==target):
            return True 

        return False

    '''

        