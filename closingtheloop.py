n = int(input())



for a in range(n):
    _ = input()

    blues = []
    reds = []

    ropes = input().split()

    for x in ropes:
        if 'B' in x:
            blues.append(int(x[:-1]))
        else:
            reds.append(int(x[:-1]))

    blues.sort(reverse=True)
    reds.sort(reverse=True)
    max_len = 0
    for i in range(min(len(blues), len(reds))):
        max_len += blues[i] + reds[i] - 2

    
    print("Case #{}: {}".format(a+1, max_len))



