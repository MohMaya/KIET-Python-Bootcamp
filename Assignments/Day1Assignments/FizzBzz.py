p=input("enter the number")
p=int(p)
for l in range(p):
    if l%5 == 0:
        print('buzz')
    elif l%3==0:
        print('fizz')
    elif l%15==0:
        print('fizzbuzz')
    else:
         print(l)
