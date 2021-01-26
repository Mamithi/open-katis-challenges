found_at = []


for i in range(5):
    blimp = input()
    if 'FBI' in blimp:
        found_at.append(i+1)

if len(found_at) < 1:
    print('HE GOT AWAY!')
else:
    print(' '.join([str(x) for x in found_at]) )