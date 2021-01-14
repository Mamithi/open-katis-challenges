a = input()
questions_list = a.split(';')


count = 0
for questions in questions_list:
    questions = questions.split('-')
    if len(questions) == 1:
        count += 1
    else:
        count += len(list(range(int(questions[0]), int(questions[1])+1)))

print(count)


