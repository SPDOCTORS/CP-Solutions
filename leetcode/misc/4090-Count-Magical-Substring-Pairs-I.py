class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n=len(s)
        count=0
        for j in range(n-1):
            left_freq=[0]*27
            right_freq=[0]*27
            seen=set()
            for i in range(j,-1,-1):
                seen.add(s[i])
                left_freq[len(seen)]+=1
            seen1=set()
            for i in range(j+1,n):
                seen1.add(s[i])
                right_freq[len(seen1)]+=1
            for d in range(1,27):
                count+=left_freq[d]*right_freq[d]
        return count
        