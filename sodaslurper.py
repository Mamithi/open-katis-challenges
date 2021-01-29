e, f, c = map(int, input().split())

bottles = e + f
taken = 0

while(bottles >= c):
    bottles = (bottles - c) + 1
    taken += 1

print(taken)
