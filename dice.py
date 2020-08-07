a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    b, a = a, b

for i in range(a+1, b+2):
    print(i)


