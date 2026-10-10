class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k=k1+k2
        diff=[]
        for i in range(len(nums1)):
            diff.append(abs(nums1[i]-nums2[i]))
        if k>=sum(diff):
            return 0
        diff.sort(reverse=True)
        count=1
        for i in range(1,len(diff)):
            largest=diff[i-1]
            next_largest=diff[i]           
            operations=(largest-next_largest)*count
            if k>=operations:
                k-=operations
            else:
                q = k // count
                r = k % count
                target=largest-q
                for j in range(count):
                    diff[j]=target
        
                for j in range(r):
                    diff[j]-=1
                ans=0
                for j in range(len(diff)):
                    ans+=diff[j]**2
                return ans
            count+=1
        n = len(diff)
        q = k // n
        r = k % n
        target = diff[-1] - q

        for j in range(n):
            diff[j] = target

        for j in range(r):
            diff[j] -= 1

        ans = 0
        for j in range(n):
            ans += diff[j] ** 2

        return ans



        