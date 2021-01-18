import math

n = int(input())

for _ in range(n):
    v, ang, x1, h1, h2 = map(float, input().split())

    g = 9.81

    t = x1 / (v * (math.cos(math.radians(ang))))

    y = (v * t * (math.sin(math.radians(ang)))) - (0.5 * g * (t ** 2))

    if h1 + 1 > y or h2 - 1 < y:
        print('Not safe')
    else:
        print('Safe')