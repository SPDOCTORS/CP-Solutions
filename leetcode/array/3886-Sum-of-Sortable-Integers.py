from math import isqrt
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        divisors=[]
        for i in range(1,isqrt(n)+1):
            if n%i==0:
                divisors.append(i)
                if i!=n//i:
                    divisors.append(n//i)
        for k in divisors:
            valid=True
            prev_block=None
            for i in range(0,n,k):
                blocks=nums[i:i+k]
                decrease=0
                for j in range(len(blocks)-1):
                    if blocks[j]>blocks[j+1]:
                        decrease+=1
                if blocks[-1]>blocks[0]:
                    decrease+=1
                if decrease>1:
                    valid=False
                    break      
                if prev_block is not None:
                    if max(prev_block)>min(blocks):
                        valid=False
                        break
                prev_block=blocks
            if valid:
                ans+=k
        return ans          
        