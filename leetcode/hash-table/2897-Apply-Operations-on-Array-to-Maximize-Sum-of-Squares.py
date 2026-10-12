class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        cnt=[0]*31
        for num in nums:
            for i in range(30):
                if num&(1<<i):
                    cnt[i]+=1
        ans=0
        for _ in range(k):
            x=0
            for i in range(31):
                if cnt[i]>0:
                    x|=1<<i
                    cnt[i]-=1
            ans=(ans+x**2)%mod
        return ans