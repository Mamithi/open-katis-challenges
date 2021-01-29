emma = list(map(int, input().split()))
gunnar = list(map(int, input().split()))

emma_prob = sum(emma)
gunnar_prob = sum(gunnar)

if emma_prob < gunnar_prob:
    print("Emma")
elif gunnar_prob < emma_prob:
    print("Gunnar")
else:
    print("Tie")