class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        mod=10**9+7
        ans=0
        odd=0
        even=0
        newodd=0
        neweven=0
        for num in arr:
            if num%2==0:
                even+=1
            else:
                newodd=even+1
                neweven=odd
                odd,even=newodd,neweven
            ans+=odd
        return ans%mod



        