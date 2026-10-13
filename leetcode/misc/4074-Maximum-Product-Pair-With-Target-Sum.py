class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        max_product=float('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target and nums[i]!=nums[j]:
                    if nums[i]*nums[j]>max_product:
                        max_product=nums[i]*nums[j]
                        if nums[i]>nums[j]:
                            ans=[i,j]
                        else:
                            ans=[j,i]
        return ans if ans else [-1,-1]

        