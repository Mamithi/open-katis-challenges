cost = float(input())
n = int(input())

total_space = 0
for i in range(n):
    w, l = map(float, input().split())
    total_space += w * l

print("{:.7f}".format(cost * total_space))
