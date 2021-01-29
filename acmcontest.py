res = input().split(' ')

problems, time = 0, 0

questions = []

while(int(res[0]) != -1):
    if res[2] == 'right':
        time += int(res[0])
        problems += 1

        for i in questions:
            if i[1] == res[1]:
                time += 20

    questions.append(res)
    res = input().split(' ')

print(problems, time)