class Solution:
    def countPrimes(self, n: int):
        if(n<=2):
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        i = 2
        while(i*i<n):

            if prime[i]:

                j = i * i

                while(j<n):
                    prime[j] = False
                    j += i

            i += 1

        return sum(prime)             
        
                  
         

        
                
        