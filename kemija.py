encoded = input()
decoded = ''

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

while count < len(encoded):
    decoded += encoded[count]
    if encoded[count] in vowels:
        count += 3
    else:
        count += 1

print(decoded)



