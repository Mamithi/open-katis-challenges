n = int(input())

rev = []
for i in range(n):
    a = int(input())
    rev.append(a)

rev.reverse()

for a in rev:
    print(a)
