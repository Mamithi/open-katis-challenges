n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
