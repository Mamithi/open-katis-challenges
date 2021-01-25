n = int(input()) 

friends = []

for i in range(n):
   data = list(map(str, input().split()))
   friends.append(data)

for friend in friends:
    print(friend[2])

