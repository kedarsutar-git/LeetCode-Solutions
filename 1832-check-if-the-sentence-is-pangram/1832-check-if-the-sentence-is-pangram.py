class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter = "abcdefghijklmnopqrstuvwxyz"
        for char in letter:
            if(char not in sentence):
                return False

        return True 

        