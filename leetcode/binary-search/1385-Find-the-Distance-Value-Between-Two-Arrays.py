class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=0
        arr2.sort()
        for x in arr1:
            idx=bisect.bisect_left(arr2,x)
            if idx==len(arr2) or abs(x-arr2[idx])>d:
                if idx==0 or abs(x-arr2[idx-1])>d:
                    cnt+=1
        return cnt