_ = int(input())
bats = map(int, input().split())
sum = 0
bases = 0

for bat in bats:
    if bat != -1:
        sum += bat
        bases += 1

print(sum/bases)

    