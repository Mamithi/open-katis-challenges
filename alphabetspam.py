msg = input()

lower_count = 0
upper_count = 0
whitespace = 0
symbols = 0

for i in msg:
    if i.isalpha() and i.islower():
        lower_count += 1
    elif i.isalpha() and i.isupper():
        upper_count += 1
    elif i == '_':
        whitespace += 1
    else:
        symbols += 1

print("{:.16f}".format(whitespace / len(msg)))
print("{:.16f}".format(lower_count / len(msg)))
print("{:.16f}".format(upper_count / len(msg)))
print("{:.16f}".format(symbols / len(msg)))

