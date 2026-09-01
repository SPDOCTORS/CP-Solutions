t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    answer=(n//k)*k+min(n%k,k//2)
    print(answer)