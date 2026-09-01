t=int(input())
for _ in range(t):
    n,f,a,b=map(int,input().split())
    m=list(map(int,input().split()))
    prev=0
    for i in range(n):
        gap=m[i]-prev
        f-=min(gap*a,b)
        if f<=0:
            print("NO")
            break
        prev=m[i]
    else:
        print("YES")