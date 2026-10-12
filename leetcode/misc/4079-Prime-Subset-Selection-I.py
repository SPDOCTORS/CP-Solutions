class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        prime=[True]*(n+1)
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j]=False
        ans=[]
        total=0
        for j in range(2,n+1):
            if prime[j]:
                if total+j<=s:
                    total+=j
                    ans.append(j)
        return ans



                
            
                
            
        
        