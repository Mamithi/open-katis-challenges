all = []
for i in range(5):
    all.append(map(int, input().split()))

all_marks = []

max = 0
index = 0
final_index = 0
for single in all:
    total = 0
    for marks in single:
        total += marks
    index += 1
    if total > max:
        max = total
        final_index = index
    

print(final_index, max)