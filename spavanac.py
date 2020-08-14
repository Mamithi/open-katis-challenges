h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
if m < 45:
    diff = 45-m
    if h == 0:
        new_hour = 23
    else:
        new_hour = h -1
    print(new_hour, 60-diff)