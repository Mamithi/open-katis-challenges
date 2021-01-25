msg = list(input())

s = int((len(msg)) / 2)


str1 = msg[:s]
str2 = msg[s:]

sumstr1 = [ord(i)%65 for i in str1]
sumstr2 = [ord(i)%65 for i in str2]


rotValue1 = sum(sumstr1)
rotValue2 = sum(sumstr2)

newstr1 = [(x+rotValue1)%26 for x in sumstr1]
newstr2 = [(x+rotValue2)%26 for x in sumstr2]

finalstr = [chr((newstr1[i]+newstr2[i])%26+65) for i in range(0, s)]

print(''.join(finalstr))

