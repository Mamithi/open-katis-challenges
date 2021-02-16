n = int(input())

for x in range(n):
    g = int(input())
    c = list(map(int, input().split()))
    count  = [i for i in c if c.count(i) != 2]
    print("Case #{}: {}".format(x+1, count[0]))
        
