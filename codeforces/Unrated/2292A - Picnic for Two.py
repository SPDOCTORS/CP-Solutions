import math
t=int(input())
for _ in range(t):
    l,a,b=map(int,input().split())
    x=l//math.gcd(l,a)
    y=l//math.gcd(l,b)
    print(math.gcd(x,y))