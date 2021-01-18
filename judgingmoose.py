l, r = map(int, input().split())

if l == r and l > 0:
    print("Even", l*2)
elif l != r:
    if l > r:
        print("Odd", l*2)
    else:
        print("Odd", r*2)
else:
    print("Not a moose")