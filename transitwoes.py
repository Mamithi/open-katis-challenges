s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

tt = s

for i in range(n):
    tt += d[i]
    tt += abs(tt-c[i]) % c[i]
    tt += b[i]

tt += d[n-1]

if t > tt:
    print('yes')
else:
    print('no')