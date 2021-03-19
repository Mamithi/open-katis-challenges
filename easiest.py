def add_num(num):
    rem = sum =0
    while num > 0:
        rem = num%10
        sum = sum+rem
        num = num//10
    return sum 



while True:
    n = int(input())
    if n == 0:
        break
    m = 11
    while True: 
        p = n * m        

        if add_num(p) == add_num(n):
            print(m)
            break

        m += 1

       