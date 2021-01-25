import math

while True:
    D, V = map(int, input().split())
    if D == 0 and V == 0:
        break

    d = D**3 - 6*V/math.pi
   
    small_d = pow(d, 1/3.0)


    print("{:.9f}".format(small_d))

    
