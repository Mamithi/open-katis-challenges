words = input().split()

duplicates = [x for i, x in enumerate(words) if x in words[:i]]

if len(duplicates) > 0:
    print('no')
else:
    print('yes')
   