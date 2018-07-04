def spiralOrder(A):
        ret = []
        left = 0
        right = len(A[0])-1
        top = 0
        bottom = len(A)-1
        count = len(A[0])*len(A)
        outer_loop_var=0
        while(outer_loop_var <= count):
            #Horizontal Left to Right
            j=top
            for i in range(left,right+1):
                ret.append(A[j][i])
                outer_loop_var = outer_loop_var + 1
            top = top+1

            if(outer_loop_var >= count):
                return ret

            #Vertical top to bottom
            j = right
            for i in range(top, bottom+1):
                ret.append(A[i][j])
                outer_loop_var = outer_loop_var + 1
            right = right-1

            if(outer_loop_var >= count):
                return ret

            #Horizontal from Right to Left
            j=bottom
            for i in range(right, left-1, -1):
                ret.append(A[j][i])
                outer_loop_var = outer_loop_var + 1
            bottom = bottom -1

            if(outer_loop_var >= count):
                return ret

            #Vertical From Bottom to Top
            j=left
            for i in range(bottom, top-1, -1):
                ret.append(A[i][j])
                outer_loop_var = outer_loop_var + 1
            left = left+1

            if(outer_loop_var >= count):
                return ret


my_mat = [[1,2,3][4,5,6][7,8,9]]
print(spiralOrder(my_mat))
