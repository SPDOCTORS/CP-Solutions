t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = []
    ans.append(0)
    for i in range(1, n):
        if len(ans)==k:
            break
        if c[i]==c[ans[-1]]:
            ans.append(i)
    last_ans=[]
    last_ans.append(n-1)
    for i in range(n - 2, -1, -1):
        if len(last_ans) == k:
            break

        if c[i] == c[last_ans[-1]]:
            last_ans.append(i)
    if len(ans) < k or len(last_ans) < k:
        print("NO")

    elif c[0] == c[n - 1]:
        print("YES")

    elif ans[-1] < last_ans[-1]:
        print("YES")

    else:
        print("NO")