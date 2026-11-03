
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    current_sum = a[0]
    maxi = a[0]

    for i in range(1, n):
        if a[i] % 2 != a[i - 1] % 2:
            current_sum = max(a[i], current_sum + a[i])
        else:
            current_sum = a[i]

        maxi = max(maxi, current_sum)

    print(maxi)
