cards = list(input().split())

ranks = [rank[0] for rank in cards]
total_val = 1
counts = 0

for i in range(5):
    counts = ranks.count(ranks[i])
    if counts > total_val:
        total_val = counts
    
print(total_val)


