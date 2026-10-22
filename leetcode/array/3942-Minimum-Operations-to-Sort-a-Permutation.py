class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        inc=0
        dec=0
        for i in range(n):
            next_index=(i+1)%n
            if nums[i]<nums[next_index]:
                inc+=1
            if nums[i]>nums[next_index]:
                dec+=1
        k=nums.index(0)
        if dec==1:
            return min(k,n-k+2)
        elif inc==1:
            return min(n-k,k+2)
        else:
            return -1
                
            
        