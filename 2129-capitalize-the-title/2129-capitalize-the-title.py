class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        word_title = []
        for word in words:
            if(len(word)<=2):
                word_title.append(word.lower())

            else:
                word_title.append(word.capitalize())

                
        return " ".join(word_title)
        