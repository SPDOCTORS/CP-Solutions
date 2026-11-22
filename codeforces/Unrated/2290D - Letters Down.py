t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    operations=set()
    for i in range(n//2):
        left=s[i]
        right=s[n-1-i]
        small=min(left,right)
        large=max(left,right)
        for j in range(ord(large),ord(small),-1):
            operations.add(j)
    print (len(operations))