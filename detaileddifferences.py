n = int(input())

for _ in range(n):
    a = input()
    b = input()


    res = [""] * len(a)

    for i in range(len(a)):
        if a[i] == b[i]:
            res[i] = "."
        else:
            res[i] = "*"

    print(a)
    print(b)
    print("".join(res))
    print("\n")