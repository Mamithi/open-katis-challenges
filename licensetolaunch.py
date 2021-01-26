_ = input()
days = list(map(int, input().split()))

val, idx = min((val, idx) for (idx, val) in enumerate(days))

print(len(days[:idx]))