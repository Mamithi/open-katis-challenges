a, b, c = map(int, input().split())

jumps = 0

if(b - a >= c -b and a+2 != c):
   b, c = a + 1, b
   jumps += 1

while(a+2 != c):
    a, b = b, b + 1
    jumps += 1

print(jumps)


