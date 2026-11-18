class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_char = set(allowed)
        count = 0

        for word in words:
            if all(char in allowed_char for char in word):
                count += 1

        return count 
