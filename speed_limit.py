a = int(input())
while a != -1:
    distance = 0
    previous = 0

    for i in range(a):
        speed, current = [int(x) for x in input().split()]
        distance += speed * (current - previous)
        previous = current

    print(distance, "miles")
    a = int(input())