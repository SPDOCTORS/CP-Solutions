t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    ans=0
    bonus=[]
    for x in s:
        if x>0:
            bonus.append(x)
        else:
            if bonus:
                largest=max(bonus)
                ans+=largest
                bonus.remove(largest)
    print(ans)