cards = list(input())

check_dups = set(cards)

if len(cards) == len(check_dups):
    print(1)
else:
    print(0)
