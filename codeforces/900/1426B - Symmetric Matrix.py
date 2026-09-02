t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    found=False
    for _ in range(n):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if b==c:
            found=True
    if m%2==1:
        print("NO")
    elif found:
        print("YES")
    else:
        print("NO")