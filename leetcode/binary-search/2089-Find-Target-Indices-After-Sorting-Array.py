class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt1=0
        cnt2=0
        for num in nums:
            if num<target:
                cnt1+=1
            elif num==target:
                cnt2+=1
        ans=list(range(cnt1,cnt1+cnt2))
        return ans
        