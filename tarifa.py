x = int(input())
n = int(input())

available = x

for i in range(n):
    p = int(input())
    available = available - p
    available = available + x

print(available)
    