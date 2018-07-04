def trailingZeroes(A):
        count=0
        denominator = 5
        while(A//denominator >= 1):
            count += A//denominator
            denominator *= 5
        return count

x = int(input("Enter the number : "))
print(trailingZeroes(x))
