crypto = input()
word = 'PER'


crypto_list = [crypto[i:i+3]  for i in range(0, len(crypto), 3)]

days = 0
for i in range(len(crypto_list)):
    test_word = crypto_list[i]
    for j in range(len(test_word)):
        if test_word[j] != word[j]:
            days += 1

print(days)