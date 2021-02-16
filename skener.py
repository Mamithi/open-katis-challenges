r, c, zr, zc = map(int, input().split())

for i in range(r):
    row = input()
    out = ""
    for j in range(c):
        out += row[j] *zc
    print((out+ "\n")*zr)
