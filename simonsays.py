n = int(input())

for _ in range(n):
    inst = input()

    check = 'Simon says'
    first = inst[:len(check)]

    if first == check:
        print(inst[len(check)+1:])