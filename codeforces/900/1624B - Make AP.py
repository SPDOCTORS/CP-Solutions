t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    target_a=2*b-c
    target_b=a+c
    target_c=2*b-a
    if target_a>0 and target_a%a==0:
        print("YES")
    elif target_b>0 and target_b%(2*b)==0:
        print("YES")
    elif target_c>0 and target_c%c==0:
        print("YES")
    else:
        print("NO")