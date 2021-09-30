n, k = map(int, input().split())

rated = 0

if k > 0:
    for _ in range(k):
        rated += int(input())


unrated = 0

if k < n:
    unrated = n - k

min_unrated = 0
max_unrated = 0

if unrated > 0:
    min_unrated = unrated * -3
    max_unrated = unrated * 3


min_total = (min_unrated + rated) / n
max_total = (max_unrated + rated) / n

print(min_total)
print(max_total)
