_ = input()

expenses = map(int, input().split())

spent = 0

for i in expenses:
    if i < 0:
        spent -= i
print(spent)