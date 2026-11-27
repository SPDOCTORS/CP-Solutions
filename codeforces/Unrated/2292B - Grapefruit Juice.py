t = int(input())

for _ in range(t):
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    prefix = []
    sumi = 0

    for x in a:
        sumi += x
        prefix.append(sumi)

    maxi = 0

    for j in range(n // k + 1):
        fresh = n - (j * k)

        if fresh > 0:
            fresh_sum = prefix[fresh - 1]
        else:
            fresh_sum = 0

        juice_sum = j * p

        total = fresh_sum + juice_sum
        maxi = max(maxi, total)

    print(maxi)