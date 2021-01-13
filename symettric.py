n = int(input())

while(n != 0):
    for i in range(n):
        word = input()
        if word.isnumeric() and int(word) == 0:
            exit()
        if word.isnumeric() and int(word) != 0:
            n = int(word)

            
        

        
