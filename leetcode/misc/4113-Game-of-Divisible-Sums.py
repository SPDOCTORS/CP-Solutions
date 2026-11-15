class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[0,0]for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for turn in range(2):
                s=nums[i]
                next_turn=1-turn if s%3==0 else turn
                take_one=(s if turn==0 else -s) +dp[i+1][next_turn]
                if i+1<n:
                    s=nums[i]+nums[i+1]
                    next_turn=1-turn if s%3==0 else turn
                    take_two=(s if turn==0 else -s) +dp[i+2][next_turn]
                    if turn==0:
                        dp[i][turn]=max(take_one,take_two)
                    else:
                        dp[i][turn]=min(take_one,take_two)
                else:
                    dp[i][turn]=take_one
        return dp[0][0]

        