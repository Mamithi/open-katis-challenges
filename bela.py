input_str = input().split()

n = int(input_str[0])
dominant = input_str[1]

def getValue(value):
    if value == 'A':
        return 11
    if value == 'K':
        return 4
    if value == 'Q':
        return 3
    if value == 'J':
        return 2
    if value == 'T':
        return 10
    if value == '9':
        return 0
    if value == '7' or value == '8':
        return 0

def getDominantValue(value):
    if value == 'A':
        return 11
    if value == 'K':
        return 4
    if value == 'Q':
        return 3
    if value == 'J':
        return 20
    if value == 'T':
        return 10
    if value == '9':
        return 14
    if value == '7' or value == '8':
        return 0
sum = 0
for i in range(n*4):
    play =  list(input())
    if play[1] == dominant:
        sum += getDominantValue(play[0])
    else:
        sum += getValue(play[0])

print(sum)