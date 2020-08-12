l, n = map(int, input().split())

current = 0
not_allowed = 0
for i in range(n):
    action, x = input().split()
    x = int(x)
    if action == 'enter':
        if x > l:
           not_allowed += 1
        else:
            l -= x 
    else:
        l += x
print(not_allowed)