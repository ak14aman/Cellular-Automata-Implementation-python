# Code for Elementary Cellular Automata
# 3 Neighbour 1-Dimension Null Boundary Problem


# Function to determine the rule to be followed by the 3 elements
# Uncomment to use any of the logical operators as the function
def fun(a,b,c):
    return a or b or c                 #Logical OR
    #return a and b and c               #Logical AND
    #return a ^ b ^ c                   #Exclusive OR (XOR)
    #return int(not((a ^ b) ^ c))       #Exclusive NOR (XNOR)

# Function to display the 1-Dimensional vector (row)
def display(arr, n, gen):
    print(f"\n Gen {gen} : ", end=" ")
    for i in range(0,n):
        print(arr[i], end=" ")

# Function to generate the next iterations/generations
def generate(arr, n):
    t=int(input("Enter number of iterations needed: "))
    gen=1
    display(arr, n, 0)  # gen 0
    while t>0:
        narr = [None] * n
        for i in range(0,n):
            b=arr[i]

            if i==0:
                c = arr[i + 1]
                narr[i]=fun(0,b,c)
            elif i==(n-1):
                a = arr[i - 1]
                narr[i]=fun(a,b,0)
            else:
                a = arr[i - 1]
                c = arr[i + 1]
                narr[i]=fun(a,b,c)

        arr=narr
        display(narr, n, gen)
        gen+=1
        t-=1



# main section
print("Using function as Logical OR")  # Since here we have uncommented the OR operation
states = int(input("Enter total states: "))  # total number of states or basically size of the intital array
arr = []
print("Enter initial state (0 or 1): ")  # type 1/0 and press enter, then again for the next value and so on
for i in range(0, states):
    l=int(input())
    arr.append(l)

# Function generates the subsequest generations as requested by the user
generate(arr, states)

