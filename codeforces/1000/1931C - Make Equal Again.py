t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    left=0
    while i<n:
        if a[i]==a[0]:
            left+=1
            i+=1
        else:
            break
    right=0
    i=n-1
    while i>=0:
        if a[n-1]==a[i]:
            right+=1
            i-=1
        else:
            break
    if a[0]==a[n-1]:
        mini=max(0,n-left-right)
    else:
        mini=min(n-left,n-right)
    print(mini)