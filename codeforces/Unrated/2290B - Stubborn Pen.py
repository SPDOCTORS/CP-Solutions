t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    pen="R"
    for i in range(n):
        if s[i]!=pen:
            ans+=1
        if s[i]=="R":
            pen="B"
        else:
            pen="R"
    print(ans)
            