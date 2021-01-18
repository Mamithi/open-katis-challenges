steps = list(map(int, input().split()))

del steps[steps.index(max(steps))]

print(max(steps) * min(steps))