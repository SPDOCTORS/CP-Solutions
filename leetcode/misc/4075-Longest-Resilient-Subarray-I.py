class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        maxi=1
        length=1
        prev=-1
        for num in nums:
            r=num%k
            if r==prev:
                length+=1
            else:
                length=1
                prev=r
            if ((length-1)*r)%k==0:
                maxi=max(maxi,length)
        return maxi