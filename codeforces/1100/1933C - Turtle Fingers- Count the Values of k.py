t=int(input())
for _ in range(t):
    a,b,l=map(int,input().split())
    ans=set()
    x=0
    while a**x<=l:
        y=0
        while a**x*b**y<=l:
            if l%(a**x*b**y)==0:
                k=l*a**x*b**y
                ans.add(k)
            y+=1
        x+=1
    print(len(ans))
                