import math

n, w, h = map(int, input().split())

for _ in range(n):
    x = int(input())

    hyp = math.sqrt(w**2 + h**2)

    if x <= w or x <= h or x <= hyp:
        print("DA")
    else:
        print("NE")