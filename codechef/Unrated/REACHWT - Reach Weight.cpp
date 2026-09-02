# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    twokg=n//2
    onekg=n%2
    cost=twokg*30+onekg*20
    print(cost)
