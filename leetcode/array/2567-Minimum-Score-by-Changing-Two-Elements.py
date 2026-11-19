import heapq

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        a, b, c = heapq.nsmallest(3, nums)
        x, y, z = heapq.nlargest(3, nums)

        return min(x - c, y - b, z - a)

        