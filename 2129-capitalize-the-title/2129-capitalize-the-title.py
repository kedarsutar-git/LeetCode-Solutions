class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        capitalized_words = []
        
        for word in words:
            if(len(word)) <= 2:
                capitalized_words.append(word.lower())
            else:
                capitalized_words.append(word.capitalize())
        
        return ' '.join(capitalized_words)
        