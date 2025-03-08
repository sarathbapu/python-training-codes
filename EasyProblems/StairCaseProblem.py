def get_paths_climbing_stairs( n : int) :
    """
    https://leetcode.com/problems/n-th-tribonacci-number/description/


    """
    curr_stock = [0, 1, 1]
    
    if n < len(curr_stock):
        return curr_stock[n-1]
    
    for i in range( n-len(curr_stock) + 1):
        curr_stock = [ curr_stock[1], curr_stock[2], curr_stock[0]+curr_stock[1]+curr_stock[2]]
    
    return curr_stock[2]
print( get_paths_climbing_stairs(4) )
print( get_paths_climbing_stairs(25) )
print( get_paths_climbing_stairs(1) )
print( get_paths_climbing_stairs(2) )

