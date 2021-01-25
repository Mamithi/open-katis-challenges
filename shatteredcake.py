width = int(input())

n = int(input())

total_area = 0

for i in range(n):
    wi, li = map(int, input().split())

    total_area += wi * li

print(int(total_area/width))