t=int(input())
for _ in range(t):
    s=input().strip()
    blocks=1
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            blocks+=1
    a=set()
    a.add(blocks)
    for i in range(1,len(s)-1):
        if s[i-1]==s[i]==s[i+1]:
            a.add(blocks+2)
        elif s[i-1]==s[i+1]!=s[i]:
            a.add(blocks-2)
        else:
            a.add(blocks)
    print(len(a))