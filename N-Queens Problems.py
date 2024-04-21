import numpy as np
from itertools import permutations
import time

n=eval(input("Please enter the number of queens: "))

# Mark the range of queen can move to
def Queen(a,b,size):
    atk_range=np.zeros((size,size),dtype=int)
    for i in range(size):
        atk_range[b][i]=1
        atk_range[i][a]=1
        # Mark upper left diagonal
        if(a-i>=0 and b-i>=0):
            atk_range[b-i][a-i]=1
        # Mark upper right diagonal
        if(a+i<size and b-i>=0):
            atk_range[b-i][a+i]=1
        # Mark lower left diagonal
        if(a-i>=0 and b+i<size):
            atk_range[b+i][a-i]=1
        # Mark lower right diagonal
        if(a+i<size and b+i<size):
            atk_range[b+i][a+i]=1
    return atk_range

# Check the combinations are the correct solutions
def Check(table,num=0,checkerboard=[]):
    if(num==0):
        checkerboard=np.zeros((len(table),len(table)),dtype=int)
    checkerboard+=Queen(num,table[num],len(table))
    if(checkerboard[table[num]][num]==1):
        if(num==len(table)-1):
            return True
        else:
            return Check(table,num+1,checkerboard)
    else:
        return False

def PlaceQueens(size):
    a=[]
    count=0
    for i in permutations(range(size)):
        flag=False
        # Exclude combinations where queens are positioned on each other's diagonals
        for j in range(1,3):
            for k in range(size-j):
                if(abs(i[k]-i[k+j])==j):
                    flag=True
        if(flag==True):
            continue
        if(Check(i)==True):
            print(i)
            count+=1
    print("\nNumber of the solution: "+str(count))

#Get the result and run time
start=time.time()
PlaceQueens(n)
end=time.time()
print("Run time: "+str(end-start))