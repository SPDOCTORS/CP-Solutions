class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            num=nums[i]
            min_val=nums[i]
            for j in range(i,n):
                num&=nums[j]
                if nums[j]<min_val:
                    min_val=nums[j]
                if num==min_val:
                    cnt+=1
        return cnt

        