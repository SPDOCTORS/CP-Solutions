class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        mini=float('inf')
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=nums[j]
                length=j-i+1
                if length>=l and length<=r and curr_sum>0:
                    mini=min(mini,curr_sum)
        
        return mini if mini!=float('inf') else -1


        