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
    m = 10
    while True:
        p = add_num(n * m)   
        print(add_num(p))  

        if add_num(p) == n:
            print(m)
            break

        m += 1

       