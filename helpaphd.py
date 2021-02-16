n = int(input())

for _ in range(n):
    testcase = input()
    if testcase == 'P=NP':
        print("skipped")
    else:
        num = testcase.split('+')
        print(int(num[0]) + int(num[1]))
