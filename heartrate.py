n = int(input())

for i in range(n):
    b, p = input().split()
    b = int(b)
    p = float(p)

    min = ((b-1) * 60) / p
    normal = (b * 60) / p
    max = ((b+1) * 60) / p

    print("{:.4f} {:.4f} {:.4f}".format(min, normal, max))
