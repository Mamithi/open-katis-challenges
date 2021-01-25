cards = list(input())

ts = cards.count("T")
cs = cards.count("C")
gs = cards.count("G")

bonus = min([ts, cs, gs])

points = ts**2 + cs**2 + gs**2 + bonus*7

print(points)