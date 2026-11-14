t=int(input())
for _ in range(t):
    n=int(input())
    h=list(map (int,input().split()))
    h.sort()
    left=[]
    right=[]
    left.append(h[0])
    for i in range(1,n):
        if h[i]!=h[i-1]:
            left.append(h[i])
        else:
            right.append(h[i])
    right.reverse()
    ans=len(left)+len(set(right))
    arr=left+right
    print(ans)
    print(*arr)
    