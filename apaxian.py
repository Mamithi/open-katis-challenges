y, p = input().split()


name = ''

if y[-1] == 'e':
  name = y + 'x' + p

elif y[-1] == 'a' or  y[-1] == 'i' or  y[-1] == 'o' or  y[-1] == 'u':
    name = y[:-1] + 'ex' + p

elif y[-2:] == 'ex':
    name = y + p
else:
    name = y + 'ex' + p

print(name)
