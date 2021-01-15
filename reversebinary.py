a = int(input())

binary = bin(a)[2:]
output = int(str(binary[::-1]), 2)

print(output)
