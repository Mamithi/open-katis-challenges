input_n = list(map(int, input().split()))
out = list(input())

input_n.sort()
A, B, C = input_n[0], input_n[1], input_n[2]

output = []
for i in out:
    if i == 'A':
        output.append(A)
    if i == 'B':
       output.append(B)
    if i == 'C':
       output.append(C)

print(' '.join([str(i) for i in output]))



