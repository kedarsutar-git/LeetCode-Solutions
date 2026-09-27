class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        sr, sc = source
        tr, tc = target

        if(source==target): # For Same Prostion
            return 0
        
        if(sr==tr):  # Same Row 
            return 1
            
        if(sc==tc):  # Same Columns
            return 1

        if(abs(sr-tr)== abs(sc-tc)):  # same Diagonal
            return 1

        
        return 2