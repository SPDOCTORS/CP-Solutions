class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                cnt+=1
        return cnt
