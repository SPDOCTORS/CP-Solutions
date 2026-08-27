t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    freq={}
    for i in range(n):
        row=list(map(int,input().split()))
        arr.append(row)
        freq[row[0]]=freq.get(row[0],0)+1
    for x,count in freq.items():
        if count==n-1:
            p1=x
            break
    for i in range(n):
        if arr[i][0]!=p1:
            ans=[p1]+arr[i]
            break
    print(*ans)
