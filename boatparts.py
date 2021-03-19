p, n = map(int, input().split())

parts = []

for _ in range(n):
    parts.append(input())

parts_unique = []

[parts_unique.append(part) for part in parts if part not in parts_unique]



if p > len(parts_unique):
    print("paradox avoided")
else:
    part = parts_unique[p-1]
    print(parts.index(part) + 1)