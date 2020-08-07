import math

height, angle = [int(x) for x in input().split()]

hyp = height / math.sin(math.radians(angle))

print(math.ceil(hyp))