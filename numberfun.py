n = int(input())

for i in range(n):
    possible = False
    a, b, c = map(int, input().split())
    if a + b == c or a * b == c or a - b == c or b - a == c or a / b == c or b / a == c:
        print("Possible")
    else:
        print("Impossible")
    
    