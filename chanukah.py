p = int(input())
for i in range(p):
    k, n = map(int, input().split())
    count = n
    for j in range(n + 1):
        count += j
    print(k, count)