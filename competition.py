scores = [89, 43, 67, 8, 100, 89, 89, 100]
cutoff = 5



from random import randint
# scores = [randint(0, 100000) for p in range(0, 100000)]
# scores = [0 for p in range(0, 100000)]


import time

start_time = time.time()

scores.sort(reverse=True)

ranks = [1]

count = 1


for i in range(len(scores)-1):
    if scores[i] == scores[i+1]:
        ranks.append(ranks[-1])
    else:
        if len(ranks) < 2:
            ranks.append(ranks[-1] + 1)
        elif ranks[-1] == ranks[-2]:
            ranks.append(ranks[-1]+2)
        else:
            ranks.append(ranks[-1] + 1)



ranks_list = [x for x in ranks if x <= cutoff]

print(scores)
print(ranks)
print(ranks_list)
print(len(ranks_list))

print(time.time() - start_time)