t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    found = False

    for i in range(n-1):
        if s[i] == s[i+1]:
            found = True
            break

    if n % 2 != 0:
        print("NO")
    elif found:
        print("YES")
    else:
        print("NO")