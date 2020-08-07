names = input().split("-")

short_form = ""

for name in names:
    short_form += name[0]

print(short_form)