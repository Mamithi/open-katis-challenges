print( 757//10 )

def get_sum(num):
    rem = sum = 0
    while(num > 0):    
        rem = num%10    
        sum = sum + rem  
        num =  num//10

    return sum
  

n = int(input())

while(n > 0):
    sum = get_sum(n)
    if n % sum == 0:
        print(n)
        break
    else:
        n += 1

