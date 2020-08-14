l, h, w = map(int, input().split())

h1 = l-h
w1 = l-w

c1 = h*w*4
c2 = h*w1*4
c3 = h1*w*4
c4 = h1*w1*4
cakes = [c1, c2, c3, c4]
print(max(cakes))