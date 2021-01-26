cards = list(map(int, input().split()))

points = cards[0] * 3 + cards[1] * 2 + cards[2] * 1

a = ""
if points >= 8:
    a = "Province"
elif points >= 5:
    a = "Duchy"
elif points >= 2:
    a = "Estate"

b = "Gold" if points >= 6 else "Silver" if points >= 3 else "Copper"

if a == "":
    print(b)
else:
    print("{} or {}".format(a, b))



