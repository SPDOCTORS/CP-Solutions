q=int(input())
for _ in range(q):
    a,b,n,s=map(int,input().split())
    x=min(a,s//n)
    y=s-x*n
    if y<=b:
        print("YES")
    else:
        print("NO")