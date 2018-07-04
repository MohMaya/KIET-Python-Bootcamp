n=input("Enter a no.")
n=int(n)
for i in range(0,n):
    print("\n")
    for j in range(0,i+1):
        print("*",end=(''))

for k in range(0,n-1):
    print("\n")
    for l in range(n-1,k,-1):
        print("*",end=(''))
