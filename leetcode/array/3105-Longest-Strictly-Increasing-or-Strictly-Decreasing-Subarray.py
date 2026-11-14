class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxlen=1
        inc=1
        dec=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i]<nums[i-1]:
                dec+=1
                inc=1
            else:
                inc=1
                dec=1
            maxlen=max(maxlen,inc,dec)
        return maxlen
            
        