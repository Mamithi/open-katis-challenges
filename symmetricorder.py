count = 1

def shuffle(x):
    if x >= n:
        return ""
    elif x == n-1:
        return names[x]+"\n"
    return names[x]+"\n" + shuffle(x+2) + names[x+1]+"\n"
 
while True:
    n = int(input())
    if n == 0:
        break
    names = []
    for x in range(n):
        names.append(input())

    print("SET", count)
    print(shuffle(0), end='')
    count += 1