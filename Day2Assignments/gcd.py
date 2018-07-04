def generalGCD(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


def euclidGCD(x, y):

   while(y):
       x, y = y, x % y

   return x

a = 60
b= 48
print(generalGCD(a,b))
print(euclidGCD(a,b))
