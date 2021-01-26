import math

s1, s2, s3, s4 = map(int, input().split())

semip = (s1+s2+s3+s4)/2

maxArea = math.sqrt((semip-s1) * (semip - s2) * (semip - s3) * (semip - s4))
if not maxArea.is_integer():
    print("{:.15f}".format(maxArea))
else:
    print(int(maxArea))