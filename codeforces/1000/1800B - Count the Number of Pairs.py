t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    ans=0
    for i in range(26):
        ch=chr(ord('a')+i)
        low=freq.get(ch,0)
        high=freq.get(ch.upper(),0)
        ans+=min(low,high)
        leftover = abs(low - high)

        extra = min(leftover // 2, k)
        ans += extra
        k -= extra

    print(ans)