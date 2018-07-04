def wave(A):
        A.sort()
        for i in range(0, len(A), 2):
            if(i+1 < len(A)):
                A[i],A[i+1] = A[i+1],A[i]
        return A
my_lis = [1,2,3,4,5,6]
print(wave(my_lis))
