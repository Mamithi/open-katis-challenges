x = int(input())


for i in range(x):
    a = int(input())
    cities = []
    for j in range(a):
        cities.append(input())
    unique = len(list(set(cities)))
    print(unique)

        

   