L = [10,9,8,7,6, 4, 1, 2, 3] 

##takes as a parameter a list of integers named L (assume L is not empty). 
##This function returns the length of the longest run of monotonically
##increasing numbers occurring in L. 
## A run of monotonically increasing numbers
## means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.

##For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] 
##then your function should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].



def longestRun(L):
    max_counter = 0
    counter = 1
    for n in range(1, len(L) ):
        if L[n] >= L[n-1]:
            counter = counter +1
        else:
            max_counter = counter if max_counter < counter else max_counter
            counter = 1
    # If the last sequence is the largest 
    
    max_counter = counter if max_counter < counter else max_counter
    return max_counter
    
print (longestRun(L))
