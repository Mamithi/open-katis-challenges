n = int(input())

for i in range(n):
    t = list(map(int, input().split()))

    imports = 0
    for i in range(len(t)):
        if t[i+1] == 0:
            break

        if t[i+1] > t[i]*2:
            imports += t[i+1] - t[i]*2

    print(imports)