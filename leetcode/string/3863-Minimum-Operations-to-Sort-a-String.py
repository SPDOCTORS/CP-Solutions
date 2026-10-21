class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        is_sorted=True
        for i in range(n-1):
            if s[i]>s[i+1]:
                is_sorted=False
                break
        if is_sorted:
            return 0
        if n<3:
            return -1
        if s[0]==min(s) or s[-1]==max(s):
            return 1
        if (s[0]==max(s) and s[-1]==min(s) and s.count(min(s))==1 and s.count(max(s))==1):
            return 3
        else:
            return 2     