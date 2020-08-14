res = []

for i in range(10):
    num = int(input())
    res.append(num % 42)
dup = [x for i, x in enumerate(res) if x in res[:i]]
print(len(res) - len(dup))