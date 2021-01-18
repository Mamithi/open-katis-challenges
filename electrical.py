n = int(input())

outlets = 0
for _ in range(n):
    k = list(map(int, input().split()))
    total = sum(k[1::])
    
    print(total - k[0]+1)
