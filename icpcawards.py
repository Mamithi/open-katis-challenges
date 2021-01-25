n = int(input())

participants = []
winners = []

x = 0

while x < 12:
    team = input()
      
    uni = team.split(' ')[0]

    if uni not in winners:
        winners.append(uni)
        print(team)
        x += 1
    