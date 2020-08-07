_ = input()
temps = map(int, input().split())

count: int = 0

for i in temps:
    if i < 0:
        count += 1

print(count)
