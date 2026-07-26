class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        right,left = 0,0
        maxlen = 0
        true = 0
        false = 0
        while(right<len(answerKey)):

            if(answerKey[right]=="T"):
                true += 1
            
            if(answerKey[right]=="F"):
                false += 1

            while(min(true,false)>k):

                if(answerKey[left]=="T"):
                    true -=1
                if(answerKey[left]=="F"):
                    false -=1
                    
                left +=1

            length = right-left +1
            maxlen = max(maxlen,length)
                
            right +=1
        
        return maxlen

            


                



        
        