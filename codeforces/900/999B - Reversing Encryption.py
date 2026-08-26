n=int(input())
t=input()
divisors=[]
for d in range(1,n+1):
    if n%d==0:
        divisors.append(d)

for d in divisors:
    t=t[0:d][::-1]+t[d:n]
print(t)