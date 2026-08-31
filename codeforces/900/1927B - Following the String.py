t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    freq=[0]*26
    ans=[]
    for i in range(n):
        for j in range(26):
            if freq[j]==a[i]:
                ans.append(chr(ord('a')+j))
                freq[j]+=1
                break
    print(''.join(ans))