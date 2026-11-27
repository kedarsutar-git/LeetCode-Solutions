class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] =="X++":
                X += 1

            elif operations[i] == "--X" or operations[i] =="X--":
                X -= 1

        return X