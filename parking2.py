t = int(input())

for _ in range(t):
    _ = int(input())
    parkings = input().split()
    parkings = [int(i) for i in parkings]
    distance = (max(parkings) - min(parkings)) * 2
    print(distance)