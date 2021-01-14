n = int(input())

correct_answers = []
for i in range(n):
    ans = input()
    correct_answers.append(ans)


hanh_answers = correct_answers[1:]

correct_answers = correct_answers[:len(hanh_answers)]

correct = 0

for a, b in zip(hanh_answers,correct_answers):
    if a == b:
       correct += 1


print(correct)

   