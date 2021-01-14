t = int(input())

for i in range(t):
    factorial = 1
    n = int(input())
    for j in range(1, n+1):
        factorial = factorial * j

    print(factorial % 10)
