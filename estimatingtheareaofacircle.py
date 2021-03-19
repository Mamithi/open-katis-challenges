import math

while True:
    r, m, c = map(float, input().split())

    m, c = int(m), int(c)

    if m == 0:
        break


    real_area = math.pi * r**2

    estimate = c/m * (2*r) ** 2

    print(round(real_area, 9), round(estimate, 9))

    # print("{:.16f}".format(whitespace / len(msg)))
   