class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxcount = 0
        for sentence in sentences:
                count = sentence.count(" ")
                maxcount = max(maxcount,count+1)

        return maxcount

        