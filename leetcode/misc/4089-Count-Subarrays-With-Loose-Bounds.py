class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        n=len(nums)
        j=0
        count=0
        for i in range(n):
            if nums[i]<minK or nums[i]>maxK:
                j=i+1
            else:
                count+=i-j+1
        return count


        