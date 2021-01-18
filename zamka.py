def get_sum(num):
    rem = sum = 0
    while num > 0:
        rem = num%10
        sum = sum + rem
        num = num//10
    return sum




l = int(input())
d = int(input())
x = int(input())

x_list = []

for i in range(l, d+1):
    if get_sum(i) == x:
        x_list.append(i)

print(min(x_list))
print(max(x_list))