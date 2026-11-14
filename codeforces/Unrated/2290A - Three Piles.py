t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if (a - 1 == c and b + 1 == c) or (a - 1 == b and c + 1 == b) or (b - 1 == c and a + 1 == c) or (b - 1 == a and c + 1 == a) or (c - 1 == b and a + 1 == b) or (c - 1 == a and b + 1 == a):
        print("YES")
    else:
        print("NO")
    