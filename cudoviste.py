x, y = list(map(int, input().split(' ')))

output = [0, 0, 0, 0, 0]

parkings = []

for i in range(x):
    parkings.append(input())

for i in range(x - 1):
    for j in range(y - 1):
        avail = [parkings[i][j], parkings[i+1][j],parkings[i][j+1],parkings[i+1][j+1]]
        if '#' not in avail:
            output[avail.count("X")] += 1



for i in output:
    print(i)