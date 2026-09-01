t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    low=[0]*26
    high=[0]*26
    for ch in s:
        if ch.islower():
            low[ord(ch)-ord('a')]+=1
        if ch.isupper():
            high[ord(ch)-ord('A')]+=1
    ans=0
    for i in range(26):
        pair=min(low[i],high[i])
        left=abs(low[i]-high[i])
        extra=min(left//2,k)
        k-=extra
        ans+=pair+extra
    print(ans)