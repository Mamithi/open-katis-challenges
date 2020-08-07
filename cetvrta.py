x1, y1 = [ int(x) for x in input().split()]
x2, y2 = [ int(x) for x in input().split()]
x3, y3 = [ int(x) for x in input().split()]

def get_points(a, b, c):
    if a == b:
        return c
    if b == c:
        return a
    return b

x4 = get_points(x1, x2, x3)
y4 = get_points(y1, y2, y3)
print(x4, y4)