import math

questions = int(input())
answers = list(input())

adrian = list(("ABC" * math.ceil(questions/3)))
bruno = list(("BABC" * math.ceil(questions/4)))
goran = list(("CCAABB" * math.ceil(questions/6)))

a, b, g = 0, 0, 0

for i in range(questions):
    if answers[i] == adrian[i]:
        a += 1
    if answers[i] == bruno[i]:
        b += 1
    if answers[i] == goran[i]:
        g += 1

highest = max(a,b,g)
print(highest)
if a == highest:
    print("Adrian")
if b == highest:
    print("Bruno")
if g == highest:
    print("Goran")



