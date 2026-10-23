class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        ans=-1
        for i in range(n):
            if nums[i]==i:
                continue
            ans&=nums[i]
        return 0 if ans==-1 else ans 
            
        