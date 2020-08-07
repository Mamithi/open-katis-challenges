import math

n = int(input())
all = []
for i in range(n):
    all.append(int(input()))

x = 0
for num in all:
    num_list = [str(i) for i in str(num)][:-1]
    number = int("".join(num_list))
    power = [int(i) for i in str(num)][-1]
    x += math.pow(number, power)

print(int(x))
