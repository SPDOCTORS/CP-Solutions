class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        maxi=1
        for i in range(len(nums)):
            r=nums[i]%k
            for j in range(i,len(nums)):
                if nums[j]%k!=r:
                    break
                length=j-i+1
                if ((length-1)*r)%k==0:
                    maxi=max(maxi,length)
        return maxi