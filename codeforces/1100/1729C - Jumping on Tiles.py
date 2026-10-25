t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    positions={}
    for i,ch in enumerate(s,1):
        if ch not in positions:
            positions[ch]=[]
        positions[ch].append(i)
    if s[0]>s[-1]:
        keys=sorted(positions.keys(),reverse=True)
    else:
        keys=sorted(positions.keys())
    ans=[]
    for ch in keys:
        if s[0]<=ch<=s[-1] or s[-1]<=ch<=s[0]:
            ans.extend(positions[ch])
    ans.remove(1)
    ans.insert(0, 1)
    ans.remove(n)
    ans.append(n)
    cost = abs(ord(s[0]) - ord(s[-1]))
    m = len(ans)
    print(cost, m)
    print(*ans)
                