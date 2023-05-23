# GAME OF LIFE
# Initial code for debugging and trial, not of use.


# printing the matrix
def display(mat, R, C):
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()


# function to create next generation
def generate(mat, R, C):
    tmp = [[None]*C for _ in range(R)]

    # helper function to check neighbouring elements and applying rules
    def helper(mat, r,c):
        p = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        cnt = 0
        for x,y in p:
            if 0<=r+y<R and 0<=c+x<C and mat[r+y][c+x] == 1:
                cnt+=1

        # applying rules of Game of Life
        if mat[r][c] == 1:
            print("inside if")
            if cnt<2:
                return 0
            elif 2<=cnt<=3:
                return 1
            else:
                return 0
        else:
            print("inside else")
            if cnt == 3:
                print("Inside == 3")
                return 1
            else:
                return 0


    # Now interating all the values in matrix to create new generation temp matrix
    for r in range(R):
        for c in range(C):
            tmp[r][c] = helper(mat, r,c)

    # copying the values to the main matrix from temporary matrix
    for r in range(R):
        for c in range(C):
            mat[r][c] = tmp[r][c]

    #printing the next generation:
    display(mat, R, C)



# main section

# Taking matrix input from user
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = [[None]*C for _ in range(R)]
print("Enter the entries row-wise:")

# For user input
for i in range(R):  # For loop for row entries
    for j in range(C):  # For loop for column entries
        matrix[i][j]=(int(input()))


print("Initial Matrix provided by the user: ")
display(matrix, R, C)

print("Next Generation matrix: ")
generate(matrix, R ,C)





