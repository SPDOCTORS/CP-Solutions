class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        left=0
        right=len(nums)-1
        score=0
        while left<right:
            score+=nums[right]-nums[left]
            left+=1
            right-=1
        if left==right:
            score+=nums[left]
        return score
        