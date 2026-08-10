class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "{([":
                stack.append(char)
            
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (char==")" and top=="(" or char=="}" and top=="{" or char=="]" and top=="["):
                    continue 

                else:
                    return False 
        
        return not stack 



'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            
            char = s[i]
            # if opening Bracket push in the Stack 
            # if closing Bracket Stacktop check and pop

            if(char=="(" or char=="{" or char=="["):  # for opening Bracket
                stack.append(char)
            
            else:  # for closing Braket
                if(len(stack)!=0):
                    top = stack[-1]  # top value in the stack 

                    if(char==")" and top =="(" or char=="}" and top=="{" or char=="]" and top=="[" ):
                        stack.pop()

                    else:
                        return False
                
                else:
                    return False
        
        if(len(stack)==0):
            return True 
        
        else:
            return False
'''
    
        






              
        

        




        