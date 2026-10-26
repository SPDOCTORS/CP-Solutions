class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        n=len(nums)
        peaksum=0
        valleysum=0
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peaksum+=nums[i]
            if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                valleysum+=nums[i]
        return peaksum-valleysum
        