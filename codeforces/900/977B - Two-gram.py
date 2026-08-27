n=int(input())
s=input()
freq={}
maxi=0
ans=""
for i in range(n-1):
    pairs=s[i:i+2]
    freq[pairs]=freq.get(pairs,0)+1
    for pairs in freq:
        if maxi<freq[pairs]:
            maxi=freq[pairs]
            ans=pairs
print(ans)

