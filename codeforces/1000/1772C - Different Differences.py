t = int(input())

for _ in range(t):
    k, n = map(int, input().split())

    ans = [1]
    current = 1
    diff = 1

    for i in range(1, k):
        remaining = k - i - 1

        if current + diff + remaining <= n:
            current += diff
            diff += 1
        else:
            current += 1

        ans.append(current)

    print(*ans)