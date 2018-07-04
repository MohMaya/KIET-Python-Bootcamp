def trailingZeroes(A):
        count=0
        fact = 5
        while(A/fact >= 1):
            count += A/fact
            fact *= 5
        return count

x = int(input("Enter the number : "))
print(trailingZeroes(x))
